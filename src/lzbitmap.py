#!/usr/bin/env python3
"""lzbitmap literal-class ZBM stream encoder (prototype).
Black-box derived from /usr/bin/aa -a lzbitmap I/O only. Pure Python,
no dependencies.

Covers LITERAL-ONLY streams: every 32KB chunk is incompressible (oracle
emits 00 + raw, no match section). Verified byte-identical vs oracle on
random (match-free) inputs 0..100000 bytes, single + multi chunk.

MATCH CLASS PARKED: any input where the oracle finds a long match
(runs/periodic/mixed with a repeat >= ~137 bytes) takes a different
grammar (bitmap prefix, 34/44/f3 match descriptors, fc epilogue) that
is globally planned (same local match encodes differently by context)
and is NOT replicated here. zbm_encode_literal() emits valid ZBM for
such inputs (oracle decoder accepts) but bytes differ from oracle.

Grammar (bedded, all integers little-endian):
  stream = magic(5a424d) ver(09) u16 X 00 u16 hunc body [trailer]
  trailer = 06 00 00 00 00 00, present iff total unc > 0
  X = len(first-section excluding trailer) + 5
  single (unc <= 32768): hunc = unc; first-section = body
    empty: body = 00
    nonempty: body = 00 + raw
  chunked (unc > 32768): hunc = 32768; section0 = 00 + raw[0:32768]
    section[i>=1] = u16(6+r) 00 u16(r) 00 + raw, r = chunk length
    (X2 = section length excluding final trailer)

Outer pbzb framing lives in wrap_pbzb() below (same 12B prefix +
16B chain + 15/16 store rule as the other codecs, bedded NOTE-008).
"""
import os
import struct
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

CHUNK = 32768


def zbm_encode_literal(inner):
    """Literal-only ZBM stream for match-free input -> bytes (oracle-identical
    iff oracle also finds no match in any 32KB chunk)."""
    inner = bytes(inner)
    n = len(inner)
    if n == 0:
        return b"ZBM\x09" + struct.pack("<H", 6) + b"\x00" + struct.pack("<H", 0) + b"\x00"
    if n <= CHUNK:
        body = b"\x00" + inner
        return (b"ZBM\x09" + struct.pack("<H", len(body) + 5) + b"\x00"
                + struct.pack("<H", n) + body + b"\x06\x00\x00\x00\x00\x00")
    out = [b"ZBM\x09" + struct.pack("<H", CHUNK + 6) + b"\x00" + struct.pack("<H", CHUNK)]
    out.append(b"\x00" + inner[:CHUNK])
    for i in range(CHUNK, n, CHUNK):
        c = inner[i:i + CHUNK]
        out.append(struct.pack("<H", 6 + len(c)) + b"\x00"
                     + struct.pack("<H", len(c)) + b"\x00" + c)
    out.append(b"\x06\x00\x00\x00\x00\x00")
    return b"".join(out)


def wrap_pbzb(inner, blocksize=4 * 1024 * 1024):
    """pbzb outer: split inner by blocksize; per block ZBM-literal payload
    iff c*16 <= u*15 else raw store (15/16 rule, NOTE-008)."""
    inner = bytes(inner)
    blocks = [inner[i:i + blocksize] for i in range(0, len(inner), blocksize)] or [b""]
    framed = []
    for blk in blocks:
        comp = zbm_encode_literal(blk)
        if len(comp) * 16 <= len(blk) * 15:
            framed.append((len(blk), comp))
        else:
            framed.append((len(blk), blk))
    out = [struct.pack(">4sIIIIII", b"pbzb", 0, blocksize, 0,
                       framed[0][0], 0, len(framed[0][1]))]
    for i, (u, payload) in enumerate(framed):
        out.append(payload)
        if i + 1 < len(framed):
            nu, npay = framed[i + 1][0], len(framed[i + 1][1])
            out.append(struct.pack(">IIII", 0, nu, 0, npay))
    return b"".join(out)


if __name__ == "__main__":
    sys.path.insert(0, _HERE)
    from rawenc import build_inner
    inner = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(wrap_pbzb(inner))
