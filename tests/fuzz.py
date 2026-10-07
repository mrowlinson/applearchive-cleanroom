#!/usr/bin/env python3
"""fuzz.py — seeded corruption differential driver (AAR decode).
Modes: orac (oracle-vs-C) | proto (C-vs-proto). Deterministic by seed.
Hard bar per iter: exit-class agree + no signal/timeout/hang either
side. Tree sig (mode+content, NO mtime: creation-time race on
corrupt inputs) must agree when both exit 0, EXCEPT flips landing
in compressed payload bytes: corrupt-codec recovery is
implementation-defined, reported as DIVERGENCE (counted, listed,
non-fail). Tree-diff with all flips outside compressed regions =
STRUCTURAL FAIL. fifo-mixed excluded in orac mode (oracle hangs by
design, DPROBE-04 Q1).
Usage: fuzz.py MODE ITERS SEED WORKDIR
Env: AAD_BIN (C binary), ZBM_DYLIB (proto lzbitmap; else that fixture skips).
Exit 0 all green / 1 any FAIL / 2 harness error.
"""
import os
import random
import shutil
import stat
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
VEC = os.path.join(ROOT, "vectors", "selfgen", "aar")
ORACLE_AD = os.path.join(ROOT, "harness", "oracle-adapter.sh")
PROTO = os.path.join(ROOT, "proto", "aad.py")
C_BIN = os.environ.get("AAD_BIN", "")


def sig(root):
    d = {}
    for dp, dn, fn in os.walk(root):
        for n in sorted(dn + fn):
            p = os.path.join(dp, n)
            try:
                s = os.lstat(p)
            except FileNotFoundError:
                continue
            if os.path.islink(p):
                v = ("link", os.readlink(p))
            elif os.path.isfile(p):
                with open(p, "rb") as f:
                    v = ("file", f.read())
            else:
                v = ("other", stat.S_IFMT(s.st_mode))
            d[os.path.relpath(p, root)] = (oct(s.st_mode), v)
    return d


def compressed_regions(data):
    """File offsets inside COMPRESSED block payloads (own outer walk).
    None = walk failed (conservative: caller treats as structural)."""
    if data[:4] in (b"AA01", b"YAA1"):
        return []
    if len(data) < 28 or data[:3] != b"pbz":
        return None
    regs, off, n = [], 12, len(data)
    while off < n:
        if off + 16 > n:
            return None
        unc = int.from_bytes(data[off + 4:off + 8], "big")
        comp = int.from_bytes(data[off + 12:off + 16], "big")
        if off + 16 + comp > n:
            return None
        if comp != unc:
            regs.append((off + 16, off + 16 + comp))
        off += 16 + comp
    return regs if off == n else None


def run(argv, timeout):
    try:
        r = subprocess.run(argv, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL, timeout=timeout)
        return ("exit", r.returncode if r.returncode >= 0 else 128 - r.returncode)
    except subprocess.TimeoutExpired:
        return ("timeout", -1)
    except Exception:
        return ("error", -2)


def run_oracle(aar, outdir):
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir, exist_ok=True)
    return run(["sh", ORACLE_AD, "aar-decode", aar, outdir], 25)


def run_c(aar, outdir):
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir, exist_ok=True)
    return run([C_BIN, aar, outdir], 10)


def run_proto(aar, outdir):
    shutil.rmtree(outdir, ignore_errors=True)
    os.makedirs(outdir, exist_ok=True)
    return run(["python3", PROTO, aar, outdir], 30)


def eclass(res):
    k, v = res
    if k != "exit":
        return k
    return "ok" if v == 0 else "err%d" % v


def main():
    mode, iters, seed, work = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    os.makedirs(work, exist_ok=True)
    assert mode in ("orac", "proto"), "bad mode"
    if not (C_BIN and os.access(C_BIN, os.X_OK)):
        print("HARNESS-ERROR no AAD_BIN", file=sys.stderr)
        return 2
    names = sorted(f for f in os.listdir(VEC) if f.endswith(".aar"))
    if mode == "orac":
        names = [f for f in names if f != "fifo-mixed.aar"]
    if mode == "proto" and not os.environ.get("ZBM_DYLIB"):
        names = [f for f in names if f != "hello-lzbitmap.aar"]
        print("note: ZBM_DYLIB unset, lzbitmap fixture skipped")
    blobs = {f: open(os.path.join(VEC, f), "rb").read() for f in names}
    regs = {f: compressed_regions(blobs[f]) for f in names}
    rng = random.Random(seed)
    fails = 0
    divs = 0
    for i in range(iters):
        f = names[rng.randrange(len(names))]
        data = bytearray(blobs[f])
        flips = []
        for _ in range(rng.randrange(1, 7)):
            o = rng.randrange(len(data))
            data[o] = rng.randrange(256)
            flips.append(o)
        case = os.path.join(work, "case%d.aar" % i)
        with open(case, "wb") as fh:
            fh.write(data)
        if mode == "orac":
            r0, r1 = run_oracle(case, work + "/o%d" % i), run_c(case, work + "/c%d" % i)
            sides = ("o%d" % i, "c%d" % i)
        else:
            r0, r1 = run_c(case, work + "/c%d" % i), run_proto(case, work + "/p%d" % i)
            sides = ("c%d" % i, "p%d" % i)
        ec0, ec1 = eclass(r0), eclass(r1)
        if ec0 != ec1 or ec0 in ("timeout", "error"):
            print("FAIL %s-%d %s (%s vs %s)" % (mode, i, f, ec0, ec1))
            fails += 1
            continue
        if ec0 == "ok" and sig(os.path.join(work, sides[0])) != sig(os.path.join(work, sides[1])):
            rr = regs[f]
            rec = rr is not None and any(a <= o < b for o in flips for a, b in rr)
            if rec:
                print("DIVERGENCE %s-%d %s codec-recovery flips=%s" % (mode, i, f, sorted(flips)))
                divs += 1
            else:
                print("FAIL %s-%d %s tree-diff STRUCTURAL" % (mode, i, f))
                fails += 1
            continue
        print("PASS %s-%d" % (mode, i))
    print("%s: %d/%d agree %d divergence" % (mode.upper(), iters - fails, iters, divs))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
