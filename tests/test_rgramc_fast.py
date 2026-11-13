#!/usr/bin/env python3
# test_rgramc_fast.py -- fast equivalent of tests/test_rgram_c.sh.
# Same pins, same verdicts; one process: rgram.py imported once,
# oracle bytes from ct-cache, C binary subprocess per cell (~1ms).
# Usage: python3 tests/test_rgramc_fast.py [workdir]
#   RGRAMC=/path/rgramc (required)  CT_CACHE_DIR / CT_REAL optional.
import hashlib
import io
import os
import re
import subprocess
import sys
from contextlib import redirect_stderr, redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "src"))
WORK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.environ.get("TMPDIR", "/tmp"), "rgramc-fast")
RGRAMC = os.environ.get(
    "RGRAMC", "/Volumes/NVME/applearchive-cleanroom-ws/build/aae/rgramc")
CACHE = os.environ.get(
    "CT_CACHE_DIR", "/Volumes/NVME/applearchive-cleanroom-ws/ct-cache")
REAL = os.environ.get("CT_REAL", "/usr/bin/compression_tool")
PINS = os.path.join(ROOT, "vectors", "rgram-PINS.csv")
# FLOOR: proven covered-cell count from full regen (rgramc-regen2:
# 903 n-bands + 4571 range tiers + 2172 single-N tiers, max N 390836).
# Was 11496 at T10P387R/N<=151760 before regen.
FLOOR = 55272

if not (os.path.isfile(RGRAMC) and os.access(RGRAMC, os.X_OK)):
    sys.stderr.write("need C binary: %s (make -C src/c)\n" % RGRAMC)
    sys.exit(2)
if not os.path.isfile(PINS):
    sys.stderr.write("missing %s\n" % PINS)
    sys.exit(2)
os.makedirs(WORK, exist_ok=True)

NS = sorted(int(m.group(1)) for m in
            re.finditer(r"^g-z([0-9]+)-closed", open(PINS).read(), re.M))

import rgram as py_rgram  # noqa: E402


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
        return f.read()


fail = 0
lid = 0
cov = 0
unc = 0
se = 0
for n in NS:
    se += 1
    raw = rav_for(n)
    if raw is None:
        print("FAIL g%d ct" % n)
        fail = 1
        continue
    rp = os.path.join(WORK, "c.rav")
    with open(rp, "wb") as f:
        f.write(raw)
    old = sys.argv
    sys.argv = ["rgram.py", rp, str(n)]
    pout, perr = io.StringIO(), io.StringIO()
    try:
        with redirect_stdout(pout), redirect_stderr(perr):
            prc = py_rgram.main()
    except SystemExit as e:
        prc = e.code if isinstance(e.code, int) else 1
    finally:
        sys.argv = old
    r = subprocess.run([RGRAMC, rp, str(n)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    crc = r.returncode
    cout, cerr = (r.stdout.decode("utf-8", "replace"),
                  r.stderr.decode("utf-8", "replace"))
    if crc == 2 and "N out of scope" in cerr:
        unc += 1
        continue
    cov += 1
    if prc == crc and pout.getvalue() == cout and perr.getvalue() == cerr:
        lid += 1
    else:
        print("FAIL g%d py[%s]=%s C[%s]=%s"
              % (n, prc, pout.getvalue()[:120], crc, cout[:120]))
        fail = 1

print("RGRAMC-PYID %d/%d covered=%d/%d" % (lid, cov, cov, se))
if lid == cov and cov >= FLOOR and fail == 0:
    print("RGRAMC-GREEN")
    sys.exit(0)
print("RGRAMC-RED")
sys.exit(1)
