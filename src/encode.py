#!/usr/bin/env python3
"""encode.py SRCDIR OUT.aar [--alg raw|lzfse|zlib|lzma|lz4|lzraven] [--block SIZE] [--threads N]
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
from lz4enc import wrap_pbz4
from lzraven import wrap_pbzm, LzRavenUnclosed
from lzbitmap import wrap_pbzb, LzBitmapMatchFound


def parse_size(s):
    m = re.fullmatch(r"(\d+)([bkmg]?)", s)
    if not m:
        raise ValueError("bad size %r" % s)
    return int(m.group(1)) * {"": 1, "b": 1, "k": 1024, "m": 1024**2, "g": 1024**3}[m.group(2)]


def _usage(msg):
    sys.stderr.write("encode.py: %s\n" % msg)
    sys.stderr.write("usage: encode.py SRCDIR OUT.aar [--alg raw|lzfse|zlib|lzma|lz4|lzraven|lzbitmap] [--block SIZE] [--threads N]\n")
    raise SystemExit(2)


def _need_val(argv, i):
    if i + 1 >= len(argv):
        _usage("flag %s needs a value" % argv[i])
    return argv[i + 1]


def main(argv):
    src = out = None
    alg = "lzfse"
    block = 4 * 1024 * 1024
    threads = 1
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--alg":
            alg = _need_val(argv, i); i += 2
        elif a == "--block":
            raw = _need_val(argv, i)
            try:
                block = parse_size(raw)
            except ValueError:
                sys.stderr.write("invalid block size: %r\n" % raw)
                raise SystemExit(2)
            i += 2
        elif a == "--threads":
            raw = _need_val(argv, i)
            try:
                threads = int(raw)
            except ValueError:
                threads = 0
            if threads <= 0:
                sys.stderr.write("invalid threads: %r (want int > 0)\n" % raw)
                raise SystemExit(2)
            i += 2  # accepted, ignored (deterministic single-threaded)
        elif src is None:
            src = argv[i]; i += 1
        elif out is None:
            out = argv[i]; i += 1
        else:
            _usage("unexpected arg %r" % a)
    if src is None or out is None:
        _usage("need SRCDIR OUT.aar")
    magics = {"lzfse": b"pbze", "zlib": b"pbzz"}
    if alg not in ("raw", "lzma", "lz4", "lzraven", "lzbitmap") + tuple(magics):
        raise SystemExit("unsupported alg %r" % alg)
    if not 1 <= block <= 134217728:
        sys.stderr.write("invalid block size: %r\n" % block)
        raise SystemExit(2)
    try:
        inner = build_inner(os.fsencode(src))
    except OSError as e:
        sys.stderr.write("encode.py: cannot read %s: %s\n" % (src, e))
        raise SystemExit(1)
    if alg == "raw":
        data = inner
    elif alg == "lzma":
        data = wrap_pbzx(inner, blocksize=block)
    elif alg == "lz4":
        data = wrap_pbz4(inner, blocksize=block)
    elif alg == "lzraven":
        try:
            data = wrap_pbzm(inner, blocksize=block)
        except LzRavenUnclosed as e:
            raise SystemExit("lzraven unclosed input: %s" % e)
    elif alg == "lzbitmap":
        try:
            data = wrap_pbzb(inner, blocksize=block)
        except LzBitmapMatchFound as e:
            raise SystemExit("lzbitmap match-class input: %s" % e)
    else:
        data = wrap_pbze(inner, magic=magics[alg], blocksize=block)
    with open(out, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main(sys.argv[1:])
