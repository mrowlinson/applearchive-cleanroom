#!/usr/bin/env python3
# test_rgram_fast.py -- fast equivalent of tests/test_rgram.sh.
# Same cells, same pins, same verdicts; one process: rgram.py
# imported once, PINS loaded once, oracle served from ct-cache
# (miss path runs the real tool). Output PASS/FAIL lines match
# test_rgram.sh byte-for-byte (headers may differ).
# Usage: python3 tests/test_rgram_fast.py [workdir]
#   RGRAM_BIN=/path/rgramc  -> C leg (subprocess per cell)
#   RECORD=1                -> rewrite PINS (like .sh)
#   CT_CACHE_DIR / CT_REAL  -> cache config (defaults NVME)
import csv
import hashlib
import io
import os
import re
import subprocess
import sys
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
WORK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.environ.get("TMPDIR", "/tmp"), "rgram-fast")
PINS = os.path.join(ROOT, "vectors", "rgram-PINS.csv")
CACHE = os.environ.get(
    "CT_CACHE_DIR", "/Volumes/NVME/applearchive-cleanroom-ws/ct-cache")
REAL = os.environ.get("CT_REAL", "/usr/bin/compression_tool")
RGRAM_BIN = os.environ.get("RGRAM_BIN", "")
RECORD = os.environ.get("RECORD", "")
GEN = "test_rgram_fast.py"
try:
    OSV = subprocess.run(["sw_vers", "-productVersion"],
                         stdout=subprocess.PIPE).stdout.decode().strip()
except Exception:
    OSV = "unknown"

os.makedirs(WORK, exist_ok=True)

# Cell list: parsed from test_rgram.sh's own for-line (tracks it).
sh = open(os.path.join(HERE, "test_rgram.sh")).read()
m = re.search(r"^for s in ([0-9 ]+); do", sh, re.M)
CELLS = [int(x) for x in m.group(1).split()]

pins = {}
if not RECORD:
    with open(PINS) as f:
        for row in csv.reader(f):
            if not row or row[0].startswith("#"):
                continue
            pins[row[0]] = row[2]

rec_rows = []  # (cellN, kind, line); committed PINS = cell order, sha row first

FAIL = 0


def chk(name, check, val, nbytes):
    global FAIL
    if RECORD:
        base = name[3:-7] if name.endswith("-closed") else name[3:]
        rec_rows.append((int(base), 1 if name.endswith("-closed") else 0,
                         "%s,%s,%s,%s,%s,%s,ct-lzraven\n"
                         % (name, check, val, nbytes, GEN, OSV)))
        print("REC %s=%s" % (name, val))
        return
    exp = pins.get(name)
    if exp is None:
        print("FAIL %s: no pin" % name)
        FAIL = 1
    elif val == exp:
        print("PASS %s" % name)
    else:
        print("FAIL %s: got %s want %s" % (name, val, exp))
        FAIL = 1


def rav_for(n):
    key = hashlib.sha256(b"\x00" * n).hexdigest()
    hit = os.path.join(CACHE, key + ".rav")
    if os.path.isfile(hit):
        with open(hit, "rb") as f:
            return f.read()
    os.makedirs(CACHE, exist_ok=True)
    bp = os.path.join(WORK, "g%d.bin" % n)
    rp = os.path.join(WORK, "g%d.rav" % n)
    with open(bp, "wb") as f:
        f.write(b"\x00" * n)
    r = subprocess.run([REAL, "-encode", "-a", "lzraven",
                        "-i", bp, "-o", rp],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if r.returncode != 0:
        return None
    with open(rp, "rb") as f:
        raw = f.read()
    with open(hit, "wb") as f:
        f.write(raw)
    return raw


py_rgram = None
if not RGRAM_BIN:
    import rgram as py_rgram


def run_py(raw, n):
    rp = os.path.join(WORK, "c.rav")
    with open(rp, "wb") as f:
        f.write(raw)
    old = sys.argv
    sys.argv = ["rgram.py", rp, str(n)]
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            rc = py_rgram.main()
    except SystemExit as e:
        rc = e.code
    finally:
        sys.argv = old
    return rc, buf.getvalue()


def run_c(raw, n):
    rp = os.path.join(WORK, "c.rav")
    with open(rp, "wb") as f:
        f.write(raw)
    r = subprocess.run(RGRAM_BIN.split() + [rp, str(n)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return r.returncode, r.stdout.decode("utf-8", "replace")


print("== rgram zeros-N fast (stored + T0 + edge + T1 + T2 + T3) ==")
for n in CELLS:
    raw = rav_for(n)
    if raw is None:
        print("FAIL g%d ct rc" % n)
        FAIL = 1
        continue
    if RGRAM_BIN:
        rc, v = run_c(raw, n)
    else:
        rc, v = run_py(raw, n)
    if rc == 0:
        c = "CLOSED" if "CLOSED" in v else "BAD"
        chk("g-z%d-closed" % n, "str", c, str(len(raw)))
        chk("g-z%d" % n, "sha", hashlib.sha256(raw).hexdigest(),
            str(len(raw)))
    else:
        first = v.strip().split("\n")[0] if v.strip() else "rc=%d" % rc
        print("FAIL g%d rgram: %s" % (n, first))
        FAIL = 1

if RECORD:
    with open(PINS + ".new", "w") as pout:
        pout.write("# rgram pins: name,check,expect,bytes,generator,os,backend\n")
        pout.write("# closed = rgram grammar verdict; "
                   "sha = output hash (deterministic zeros-N)\n")
        for _, _, line in sorted(rec_rows):
            pout.write(line)
    os.replace(PINS + ".new", PINS)
    print("RECORDED %s" % PINS)
print("== %s ==" % WORK)
print("RGRAM-GREEN" if FAIL == 0 else "RGRAM-RED")
sys.exit(1 if FAIL else 0)
