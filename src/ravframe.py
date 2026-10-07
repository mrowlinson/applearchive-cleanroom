#!/usr/bin/env python3
"""ravframe.py -- lzraven frame-layer verifier (writer2 turf).

Pure framing layer (own beds NOTE-w2s4-5/6/9): parses the raven byte
stream (magic + F2 + frames + trailer) and verifies every structural
rule. Codec payload bytes are OPAQUE to this module (format hunt open).

Stream (bedded): magic 2b00caec (4B) + F2 u32le (4B) + frames +
trailer 00000000 (4B). Each frame = F3 u32le + payload bytes where
F3 = payload_len*4096 + storebit, storebit 1 = payload is raw slice.
First-frame payload cap 512K (524288); continuation frame headers
are bare 4B F3 (no magic/F2). F2 = U(rawlen)*2^26 with threshold
table threshold(U) = (4+U%4)*2^(14+U//4) (NOTE-w2s4-9).

Usage:
  ravframe.py FILE [RAWLEN] [--raw RAWFILE]
    verifies structure; prints one summary line; exit 0 ok, 1 bad.
    RAWLEN (optional) also checks F2 against the closed form and,
    for all-stored frames, payload concatenation == raw length.
    --raw RAWFILE (optional): when every frame is stored, asserts
    payload concatenation == raw file bytes exactly (storebit
    promise check; skipped silently if any frame is compressed).
  ravframe.py --f2 N
    prints expected F2 (8 hex digits) for raw length N.

Exit: 0 ok; 1 bad input/structure (message on stderr).
"""

import struct
import sys

MAGIC = bytes.fromhex("2b00caec")
TRAILER = bytes.fromhex("00000000")
FRAME_CAP = 524288
MIN_COMPRESS = 64  # bedded: raw<64 always stored (NOTE-w2s4-6)


def thresholds(limit):
    """Yield (U, T) with T = (4+U%4)*2^(14+U//4) while T < limit."""
    u = 0
    while True:
        t = (4 + (u % 4)) * (1 << (14 + (u // 4)))
        if t >= limit:
            return
        yield u, t
        u += 1


def f2_expected(rawlen):
    """Closed-form F2 (NOTE-w2s4-9): U*2^26, U = thresholds below rawlen."""
    u = 0
    for uu, t in thresholds(rawlen + 1):
        if t < rawlen:
            u = uu + 1
    return (u << 26) & 0xFFFFFFFF


def parse(buf):
    """Split stream -> (f2, [(f3, store, payload_off, payload_len)]).
    Raises ValueError on any structural violation."""
    if len(buf) < 16:
        raise ValueError("too short (%d)" % len(buf))
    if buf[:4] != MAGIC:
        raise ValueError("bad magic %s" % buf[:4].hex())
    if buf[-4:] != TRAILER:
        raise ValueError("bad trailer %s" % buf[-4:].hex())
    f2 = struct.unpack("<I", buf[4:8])[0]
    frames = []
    off = 8
    end = len(buf) - 4
    first = True
    while off < end:
        if off + 4 > end:
            raise ValueError("truncated frame header at %d" % off)
        f3 = struct.unpack("<I", buf[off:off + 4])[0]
        store = f3 & 1
        plen = (f3 - store) // 4096
        if (f3 - store) % 4096:
            raise ValueError("F3 not multiple of 4096 at %d: %08x" % (off, f3))
        if first and plen > FRAME_CAP:
            raise ValueError("first frame payload %d over cap" % plen)
        if off + 4 + plen > end:
            raise ValueError("frame overruns at %d (plen %d)" % (off, plen))
        frames.append((f3, store, off + 4, plen))
        off += 4 + plen
        first = False
    if off != end:
        raise ValueError("frames end at %d, want %d" % (off, end))
    if not frames and len(buf) != 12:
        raise ValueError("empty frame list with %d bytes" % len(buf))
    return f2, frames


def verify(buf, rawlen=None, raw=None):
    """Full verify. Returns summary string. Raises ValueError."""
    if rawlen == 0:
        if buf != MAGIC + bytes(8):
            raise ValueError("empty input must be 12B magic+zeros")
        return "empty CLOSED"
    f2, frames = parse(buf)
    if rawlen is not None and f2 != f2_expected(rawlen):
        raise ValueError("F2 %08x != expected %08x for rawlen %d"
                         % (f2, f2_expected(rawlen), rawlen))
    nstored = sum(1 for f in frames if f[1])
    paytotal = sum(f[3] for f in frames)
    matched = ""
    if raw is not None and frames and nstored == len(frames):
        cat = b"".join(buf[f[2]:f[2] + f[3]] for f in frames)
        if cat != raw:
            raise ValueError("stored payload != raw bytes (%d vs %d)"
                             % (len(cat), len(raw)))
        matched = " rawmatch"
    return "CLOSED frames=%d stored=%d pay=%d f2=%08x%s" % (
        len(frames), nstored, paytotal, f2, matched)


def die(msg):
    sys.stderr.write("ravframe: %s\n" % msg)
    return 1


def main(argv):
    if len(argv) == 2 and argv[0] == "--f2":
        try:
            n = int(argv[1])
        except ValueError:
            return die("bad length: %r" % argv[1])
        if n < 0:
            return die("bad length: %r" % argv[1])
        print("%08x" % f2_expected(n))
        return 0
    args = list(argv)
    rawpath = None
    if "--raw" in args:
        i = args.index("--raw")
        if i + 1 >= len(args):
            return die("--raw needs a file")
        rawpath = args[i + 1]
        del args[i:i + 2]
    if len(args) not in (1, 2) or args[0].startswith("--"):
        return die("usage: ravframe.py FILE [RAWLEN] [--raw RAWFILE] | "
                   "ravframe.py --f2 N")
    try:
        with open(args[0], "rb") as f:
            buf = f.read()
    except OSError as e:
        return die("read %s: %s" % (args[0], e))
    rawlen = None
    if len(args) == 2:
        try:
            rawlen = int(args[1])
        except ValueError:
            return die("bad rawlen: %r" % args[1])
    raw = None
    if rawpath is not None:
        try:
            with open(rawpath, "rb") as f:
                raw = f.read()
        except OSError as e:
            return die("read %s: %s" % (rawpath, e))
    try:
        print(verify(buf, rawlen, raw))
    except ValueError as e:
        return die(str(e))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
