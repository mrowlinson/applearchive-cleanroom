#!/usr/bin/env python3
"""rb2.py -- lzraven/lzbitmap outer frame encoder (writer2 turf).

Pure framing layer: splits a raw.aar (blocked input whole, A-14) into
blocks, applies the 15/16 store rule per block (NOTE-008), and emits
the 12B prefix + [16B header + payload]* chain (own beds NOTE-w2s3-8).

Codec bytes are INJECTED (payload files, oracle-backed at test time,
own encoder later): this module never calls any oracle or OSS.
Prototype Python per project rule; C port follows at parity.

Usage:
  rb2.py --alg lzraven|lzbitmap [--block SIZE] --payload-dir DIR
         raw.aar out.aar
  SIZE = integer + optional b/k/m/g suffix (aa CLI shape); default 4m.
  DIR holds blk%04d.bin, one per ceil(len(raw)/block) block, in order.

Exit: 0 ok; 1 bad input/flags (message on stderr).
"""

import os
import struct
import sys

MAGICS = {
    "lzraven": bytes.fromhex("70627a6d"),   # pbzm (own pin m-empty-lzraven-magic)
    "lzbitmap": bytes.fromhex("70627a62"),  # pbzb (own pin m-empty-lzbitmap-magic)
}
DEFAULT_BLOCK = 4 * 1024 * 1024  # bedded DEF-EQ-4M (NOTE-w2s3-8)
MAX_BLOCK = 128 * 1024 * 1024    # NOTE-008 range 1..128m


def parse_block(s):
    s = s.strip().lower()
    mult = 1
    if s[-1:] in ("b", "k", "m", "g"):
        mult = {"b": 1, "k": 1024, "m": 1024**2, "g": 1024**3}[s[-1]]
        s = s[:-1]
    try:
        n = int(s) * mult
    except ValueError:
        return None
    if n < 1 or n > MAX_BLOCK:
        return None
    return n


def decide_store(unc, comp):
    """15/16 rule (NOTE-008): store iff comp > floor(15*unc/16).

    16*comp > 15*unc is exactly that (equality stores: comp==unc
    gives 16u > 15u). unc > 0 always (no empty blocks).
    """
    return 16 * comp > 15 * unc


def frame(raw, magic, blocksize, payloads):
    out = [magic + struct.pack(">II", 0, blocksize)]
    nblocks = (len(raw) + blocksize - 1) // blocksize
    if len(payloads) != nblocks:
        raise ValueError("want %d payloads, got %d" % (nblocks, len(payloads)))
    for i in range(nblocks):
        blk = raw[i * blocksize:(i + 1) * blocksize]
        comp = payloads[i]
        if decide_store(len(blk), len(comp)):
            comp = blk
        out.append(struct.pack(">IIII", 0, len(blk), 0, len(comp)))
        out.append(comp)
    return b"".join(out)


def die(msg):
    sys.stderr.write("rb2: %s\n" % msg)
    return 1


def main(argv):
    alg = None
    block = DEFAULT_BLOCK
    paydir = None
    rest = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--alg" and i + 1 < len(argv):
            alg = argv[i + 1]
            i += 2
        elif a == "--block" and i + 1 < len(argv):
            block = parse_block(argv[i + 1])
            if block is None:
                return die("invalid block size: %r" % argv[i + 1])
            i += 2
        elif a == "--payload-dir" and i + 1 < len(argv):
            paydir = argv[i + 1]
            i += 2
        elif a.startswith("--"):
            return die("unknown flag: %s" % a)
        else:
            rest.append(a)
            i += 1
    if alg not in MAGICS:
        return die("need --alg lzraven|lzbitmap")
    if paydir is None:
        return die("need --payload-dir DIR")
    if len(rest) != 2:
        return die("usage: rb2.py --alg A [--block S] --payload-dir D raw.aar out.aar")
    src, dst = rest
    try:
        with open(src, "rb") as f:
            raw = f.read()
    except OSError as e:
        return die("read %s: %s" % (src, e))
    nblocks = (len(raw) + block - 1) // block
    payloads = []
    for i in range(nblocks):
        p = os.path.join(paydir, "blk%04d.bin" % i)
        try:
            with open(p, "rb") as f:
                payloads.append(f.read())
        except OSError as e:
            return die("read %s: %s" % (p, e))
    try:
        outer = frame(raw, MAGICS[alg], block, payloads)
    except ValueError as e:
        return die(str(e))
    try:
        with open(dst, "wb") as f:
            f.write(outer)
    except OSError as e:
        return die("write %s: %s" % (dst, e))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
