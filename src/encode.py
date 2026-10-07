#!/usr/bin/env python3
"""encode.py SRCDIR OUT.aar [--alg raw|lzfse|zlib|lzma] [--block SIZE] [--threads N]
Cleanroom AAR encoder (prototype). --threads accepted, single-threaded.
SIZE: integer + optional b/k/m/g suffix.
"""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from rawenc import build_inner
from pbze import wrap_pbze
from lzmaenc import wrap_pbzx


def parse_size(s):
    m = re.fullmatch(r"(\d+)([bkmg]?)", s)
    if not m:
        raise ValueError("bad size %r" % s)
    return int(m.group(1)) * {"": 1, "b": 1, "k": 1024, "m": 1024**2, "g": 1024**3}[m.group(2)]


def main(argv):
    src = out = None
    alg = "lzfse"
    block = 4 * 1024 * 1024
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--alg":
            alg = argv[i + 1]; i += 2
        elif a == "--block":
            block = parse_size(argv[i + 1]); i += 2
        elif a == "--threads":
            i += 2  # accepted, ignored (deterministic single-threaded)
        elif src is None:
            src = argv[i]; i += 1
        elif out is None:
            out = argv[i]; i += 1
        else:
            raise SystemExit("unexpected arg %r" % a)
    if src is None or out is None:
        raise SystemExit("usage: encode.py SRCDIR OUT.aar [--alg raw|lzfse|zlib] [--block SIZE] [--threads N]")
    magics = {"lzfse": b"pbze", "zlib": b"pbzz"}
    if alg not in ("raw", "lzma") + tuple(magics):
        raise SystemExit("unsupported alg %r (parked: lz4 lzraven lzbitmap)" % alg)
    if not 1 <= block <= 134217728:
        raise SystemExit("invalid block size %d (oracle range 1..134217728)" % block)
    inner = build_inner(os.fsencode(src))
    if alg == "raw":
        data = inner
    elif alg == "lzma":
        data = wrap_pbzx(inner, blocksize=block)
    else:
        data = wrap_pbze(inner, magic=magics[alg], blocksize=block)
    with open(out, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main(sys.argv[1:])
