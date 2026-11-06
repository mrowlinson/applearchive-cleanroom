#!/usr/bin/env python3
"""lzraven encoder (proto). Black-box from compression_tool I/O only.

Scope (proto): single-frame streams only.
  - n == 0                     -> 12B empty form (bedded).
  - n < 64                     -> stored frame (bedded MIN_COMPRESS).
  - zeros, 64 <= n <= 820      -> synthesized T0/T1/T2/T3 payload
                                  (closed-form tiers + in-repo tables).
  - zeros, n > 820             -> LzRavenUnclosed (honest error; sibling
                                  lanes own T4+; never emit wrong bytes).
  - non-zero, n < 64           -> stored frame (bedded MIN_COMPRESS).
  - non-zero, n >= 64          -> STORED-GUESS (PROTO GAP): general payload
                                  grammar unknown; output equals oracle iff
                                  oracle stores this input (random-like).
                                  Battery proves pinned cells byte-identical;
                                  compressible non-zero inputs (patterns,
                                  zeros-runs inside structure, AAR inners of
                                  non-random dirs) MISMATCH oracle -> loud
                                  RED, never claimed green.

Framing mirrors src/ravframe.py: magic 2b00caec + F2 (closed form) +
F3 = plen*4096 + storebit + payload + trailer 00000000.
F2 is 0 for every n in scope (first threshold at 65536).
"""

import os
import struct
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from ravframe import MAGIC, TRAILER, f2_expected
from rgram import _T2SCRAM, _T2W32, _T2W240, _T3CASC, _T3P245

RAV_SCOPE_MAX = 820  # zeros synthesis cap: T0..T3 (sibling lanes own T4+)


class LzRavenUnclosed(Exception):
    pass


def _bits_set(buf, positions, value):
    """Clear then set the listed bit positions (LSB-first) to value."""
    for j, p in enumerate(positions):
        if (value >> j) & 1:
            buf[p >> 3] |= (1 << (p & 7))
        else:
            buf[p >> 3] &= ~(1 << (p & 7))


def _t0(off):
    if off <= 60:  # n 64..124
        p = bytearray(bytes.fromhex(
            "400000000100000007000000000000000800000001000f000600000000"
            "2800000400180004000000e0000000"))
        p[4] = ((off << 1) | 1) & 0xFF
        op3 = off + 3
        _bits_set(p, (234, 235, 236, 237),
                  ((op3 >> 4) & 1) | ((1 - ((op3 >> 5) & 1)) << 1) |
                  (((op3 >> 5) & 1) << 2) | (1 << 3))
        _bits_set(p, (275, 276, 277, 278), op3 & 15)
        return bytes(p)
    # n 125..127: form flip
    p = bytearray(bytes.fromhex(
        "000400007b00000007000000000000000800000001000f000600c0010400"
        "00000000000004000000040e0000"))
    p[4] = ((off << 1) | 1) & 0xFF
    n = off + 64
    _bits_set(p, (307, 308), n - 125)
    return bytes(p)


def _t1(off):
    p = bytearray(bytes.fromhex(
        "000800000100000008000000000000000800000001000f000600c0010400"
        "0000000000000400180004100000"))
    p[4] = ((off << 1) | 1) & 0xFF
    op3 = off + 3
    _bits_set(p, (307, 308, 309, 310), op3 & 15)
    _bits_set(p, (270, 271, 272, 273), (op3 >> 4) & 15)
    return bytes(p)


# bit scatter for the T2 w332 16-bit word (verifier order)
_W332POS = (332, 334, 336, 337, 338, 339, 340, 341, 342, 343,
            344, 346, 347, 348, 349, 350)


def _t2_set_w332(p, e32):
    _bits_set(p, _W332POS, e32)


def _t2_set_window(p, off):
    """Window bytes 30/31: byte30 full, byte31 = field bits 249-253."""
    if 143 <= off <= 152:
        ew = (0x82, 0x10) if off & 1 else (0x72, 0x0f)
    else:
        ew = _T2W240[min((off - 153) >> 4, 4)]
    p[30] = ew[0]
    _bits_set(p, (249, 250, 251, 252, 253), ew[1])


def _t2(off):
    n = off + 256
    if off <= 124:
        p = bytearray(bytes.fromhex(
            "001000000100000009000000000000000800000001000f000600c00104"
            "000000000002000400180004120000"))
        p[4] = ((off << 1) | 1) & 0xFF
        op3 = off + 3
        _bits_set(p, (307, 308, 309, 310), op3 & 15)
        _bits_set(p, (270, 271, 272, 273), ((op3 >> 4) | 8) & 15)
        return bytes(p)
    if off == 125:
        return bytes.fromhex(
            "10000000fb00000009000000000000000800000001000f000600000000"
            "000f00040000000000000020010000")
    if off == 126:
        return bytes.fromhex(
            "00080000fd00000009000000000000000800000001000f000600000000"
            "3c00000400000001c00d0006480000")
    if off <= 142:
        p = bytearray(bytes.fromhex(
            "00800000ff00000009000000080000000000000001000f000600e00104"
            "0000000000000001000e0006480000"))
        p[4] = ((off << 1) | 1) & 0xFF
        if off >= 128:
            p[5] |= 0x01
        else:
            p[5] &= 0xFE
        _bits_set(p, _W332POS, (((off - 127) & 15) << 11) | 2)
        return bytes(p)
    if off == 143:
        return bytes.fromhex(
            "008000001f01000009000000080000000000000001000f000600e00104"
            "0082200000000001000f0006480001")
    if off <= 152:
        p = bytearray(bytes.fromhex(
            "008000002101000009000000080000000000000001000f000600e00104"
            "00721e0000000001000f0006486f45"))
        p[4] = ((off << 1) | 1) & 0xFF
        p[5] |= 0x01
        _t2_set_window(p, off)
        _t2_set_w332(p, _T2SCRAM[off - 144])
        return bytes(p)
    if off <= 216:
        p = bytearray(bytes.fromhex(
            "00000800330100000d000000080000000000000001000f000600e00104"
            "0082200000000001000f0006486528"))
        p[4] = ((off << 1) | 1) & 0xFF
        p[5] |= 0x01
        _bits_set(p, (51, 52, 53, 54), (off - 153) & 15)
        _t2_set_window(p, off)
        _t2_set_w332(p, _T2W32[min((off - 153) >> 4, 4)])
        return bytes(p)
    if off == 217:
        p = bytearray(bytes.fromhex(
            "00000800330100000d000000080000000000000001000f000600e00104"
            "0082200000000001000f0006486528"))
        p[0] = 0x00
        p[1] = 0x00
        p[2] = 0x80
        p[4] = ((off << 1) | 1) & 0xFF
        p[5] |= 0x01
        p[12] = 0x0c
        _bits_set(p, (51, 52, 53, 54), 0)
        _t2_set_window(p, off)
        _t2_set_w332(p, _T2W32[min((off - 153) >> 4, 4)])
        return bytes(p)
    # regC 218..255
    p = bytearray(bytes.fromhex(
        "10008000b50100000d0000000c0000000000000001000f000600e0010400"
        "82200000000001000f0006482738"))
    p[0] = (((off - 217) & 15) << 4) & 0xFF
    p[4] = ((off << 1) | 1) & 0xFF
    p[6] = 0x00 if off < 233 else (0x08 if off < 249 else 0x10)
    _t2_set_window(p, off)
    _t2_set_w332(p, _T2W32[min((off - 153) >> 4, 4)])
    return bytes(p)


def _t3(off):
    if off <= 216:
        c = off + 7
        p = bytearray(bytes.fromhex(
            "e0000001010020000e0000000c0000000000000001000f000600e00104"
            "0082200000000001000f0006502738"))
        p[0] = (((c & 7) << 5) | 0x00) & 0xFF
        p[1] = (((c >> 3) & 1) | ((1 if c == 224 else 0) << 7)) & 0xFF
        p[4] = ((off << 1) | 1) & 0xFF
        p[5] = (off >> 7) & 0xFF
        p[6] = ((((c >> 4) + 2) & 15) << 4) & 0xFF
        return bytes(p)
    if off == 217:
        return bytes.fromhex(
            "00800000b30100000a000000080000800000000001000f000600e00104"
            "8060840000000001000f000650b8fd")
    if off == 218:
        return bytes.fromhex(
            "37006000b50100000b0000000e0000000000000001000f000600e00104"
            "8060840000000001000f000650b8fd")
    if off <= 234:
        cc = off - 219
        p = bytearray(bytes.fromhex(
            "38000006b70100000b0000000e000000000000000500f0000600e00104"
            "8060840000000001000f000650b8fd"))
        p[4] = ((off << 1) | 1) & 0xFF
        p[17] = (((cc & 7) << 2) | ((cc & 8) << 3)) & 0xFF
        return bytes(p)
    if off <= 244:
        p = bytearray(bytes.fromhex(
            "3c000006d70100000b0000000e000000800042082500f0000600e00104"
            "8060840000000001000f000650b8fd"))
        p[4] = ((off << 1) | 1) & 0xFF
        p[16:20] = bytes.fromhex(_T3CASC[off - 235])
        p[20] = 0x25 if off == 235 else 0x05
        return bytes(p)
    # 245..308 settled states
    p = bytearray(bytes.fromhex(
        "3c000060eb0100000b0000000e000000d046beff0500f0000a00001e0480"
        "60840000000001000f000650b8fd"))
    p[4] = ((off << 1) | 1) & 0xFF
    p[5] = (off >> 7) & 0xFF
    p[16:20] = bytes.fromhex(_T3P245[min((off - 245) >> 4, 3)])
    p[23] = (((off - 245) & 15) << 2) & 0xFF
    return bytes(p)


def zeros_payload(n):
    """Synthesize the compressed payload for n zeros. Raises if out of scope."""
    if n <= 127:
        return _t0(n - 64)
    if n <= 255:
        return _t1(n - 128)
    if n <= 511:
        return _t2(n - 256)
    if n <= 820:
        return _t3(n - 512)
    raise LzRavenUnclosed("zeros N=%d beyond proto scope %d" % (n, RAV_SCOPE_MAX))


def encode_stream(data):
    """bytes-in -> lzraven-bit-identical bytes-out (proto scope)."""
    data = bytes(data)
    n = len(data)
    if n == 0:
        return MAGIC + bytes(8)
    if data == bytes(n):  # all zeros
        if n <= 63:
            pay, store = data, 1
        elif n <= RAV_SCOPE_MAX:
            pay, store = zeros_payload(n), 0
        else:
            raise LzRavenUnclosed("zeros N=%d beyond proto scope %d"
                                  % (n, RAV_SCOPE_MAX))
    elif n < 64:
        pay, store = data, 1
    else:
        # PROTO GAP (stored-guess): general grammar unknown; byte-identical
        # iff oracle stores this input. Battery proves pinned cells.
        pay, store = data, 1
    f3 = len(pay) * 4096 + store
    return (MAGIC + struct.pack("<I", f2_expected(n))
            + struct.pack("<I", f3) + pay + TRAILER)


def wrap_pbzm(inner, blocksize=4 * 1024 * 1024):
    """Outer pbzm framing: per-block rav stream + 15/16 store rule."""
    from rb2 import frame, MAGICS
    inner = bytes(inner)
    nblocks = (len(inner) + blocksize - 1) // blocksize or 1
    payloads = [encode_stream(inner[i * blocksize:(i + 1) * blocksize])
                for i in range(nblocks)]
    return frame(inner, MAGICS["lzraven"], blocksize, payloads)


def main(argv):
    if len(argv) != 3 or argv[0] != "--raw":
        sys.stderr.write("usage: lzraven.py --raw INFILE OUTFILE\n")
        return 2
    try:
        with open(argv[1], "rb") as f:
            data = f.read()
    except OSError as e:
        sys.stderr.write("lzraven: read %s: %s\n" % (argv[1], e))
        return 1
    try:
        out = encode_stream(data)
    except LzRavenUnclosed as e:
        sys.stderr.write("lzraven: unclosed: %s\n" % e)
        return 1
    try:
        with open(argv[2], "wb") as f:
            f.write(out)
    except OSError as e:
        sys.stderr.write("lzraven: write %s: %s\n" % (argv[2], e))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
