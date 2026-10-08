#!/usr/bin/env python3
"""lzma (pbzx) outer wrapper. Derived black-box from /usr/bin/aa I/O only.

Outer framing is pbze-identical (magic pbzx, 28B header, payloads, 16B gaps).
Per 4MB stream: XZ check-none payload whose LZMA packet bytes are stock
liblzma preset-6 (pinned: FORMAT raw-LZMA1-preset-6 lc3lp0pb2 dict-8M +
VERSION 5.8.4 + battery, per quiz A-20); block header/index/footer are
Apple-custom and rewritten here (own code): b0 = 4 iff unc >= 2**21 else 2
iff unc,comp < 128 else 3,
flags 0xC0, bcs/unpadded EXCLUDE lzma2 pad, footer crc covers back+flags,
backward = (idxlen-4)/4. Store iff 16c > 15u (razor-verified).
"""
import lzma
import os
import struct
import sys
import zlib

_PIN_VERSION = "5.8.4"
_PIN_PRESET = 6


def _vint(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(0x80 | b)
        else:
            out.append(b)
            return bytes(out)


def _read_vint(d, pos):
    n = 0
    sh = 0
    while True:
        b = d[pos]
        pos += 1
        n |= (b & 0x7F) << sh
        if not b & 0x80:
            return n, pos
        sh += 7


def _lzma2_data_end(xz, data_start):
    """End offset (pad-aligned) of the lzma2 data run starting at data_start."""
    q = data_start
    start = q
    while True:
        ctrl = xz[q]
        q += 1
        if ctrl == 0:
            eos_end = q
            while (q - start) % 4:
                if xz[q] != 0:
                    raise ValueError("bad lzma2 pad")
                q += 1
            return eos_end, q
        elif ctrl in (1, 2):
            us = struct.unpack(">H", xz[q:q + 2])[0] + 1
            q += 2 + us
        elif ctrl >= 0x80:
            rs = (ctrl >> 5) & 3
            uhi = ctrl & 0x1F
            us = (uhi << 16) + struct.unpack(">H", xz[q:q + 2])[0] + 1
            cs = struct.unpack(">H", xz[q + 2:q + 4])[0] + 1
            q += 4
            if rs >= 2:
                q += 1
            q += cs
        else:
            raise ValueError("bad lzma2 ctrl %r" % ctrl)


def oracle_xz(stock_xz, unc):
    """Rewrite one single-block stock preset-6 check-none XZ to oracle form."""
    xz = stock_xz
    if xz[:6] != bytes.fromhex("fd377a585a00") or xz[6:8] != b"\x00\x00":
        raise ValueError("not a check-none XZ stream")
    pos = 12
    b0 = xz[pos]
    hlen = (b0 + 1) * 4
    flags = xz[pos + 1]
    if flags & 0x3C or (flags & 3):
        raise ValueError("multi-filter XZ block")
    p = pos + 2
    if flags & 0x40:
        _, p = _read_vint(xz, p)
    if flags & 0x80:
        _, p = _read_vint(xz, p)
    if xz[p] != 0x21:
        raise ValueError("not an LZMA2 block")
    fsize = xz[p + 1]
    dc = xz[p + 2:p + 2 + fsize]
    data_start = pos + hlen
    eos_end, data_end = _lzma2_data_end(xz, data_start)
    if data_end % 4:
        raise ValueError("misaligned lzma2 data")
    lzdata = xz[data_start:data_end]
    # b0 rule (bedded 9+4: t119/t127->2, t128+->3, u2M->3, u3M->4):
    # 4 iff unc >= 2**21, else 2 iff both vints 1B (unc,comp < 128).
    comp = eos_end - data_start
    ob0 = 4 if unc >= (1 << 21) else (2 if unc < 128 and comp < 128 else 3)
    ohlen = (ob0 + 1) * 4
    hdr = bytearray()
    hdr.append(ob0)
    hdr.append(0xC0)
    hdr += _vint(eos_end - data_start)
    hdr += _vint(unc)
    hdr += b"\x21\x01" + dc
    while len(hdr) < ohlen - 4:
        hdr.append(0)
    if len(hdr) != ohlen - 4:
        raise ValueError("block header overflow")
    hdr += struct.pack("<I", zlib.crc32(bytes(hdr)) & 0xFFFFFFFF)
    unpadded = ohlen + (eos_end - data_start)
    idx = bytearray(b"\x00\x01")
    idx += _vint(unpadded) + _vint(unc)
    while len(idx) % 4:
        idx.append(0)
    idx += struct.pack("<I", zlib.crc32(bytes(idx)) & 0xFFFFFFFF)
    back = struct.pack("<I", (len(idx) - 4) // 4) + b"\x00\x00"
    ftr = struct.pack("<I", zlib.crc32(back) & 0xFFFFFFFF)
    ftr += back + b"YZ"
    return bytes(xz[:12]) + bytes(hdr) + lzdata + bytes(idx) + ftr


def xz_encode(chunk):
    std = lzma.compress(bytes(chunk), format=lzma.FORMAT_XZ,
                        check=lzma.CHECK_NONE, preset=_PIN_PRESET)
    return oracle_xz(std, len(chunk))


def wrap_pbzx(inner, blocksize=4 * 1024 * 1024):
    chunks = [inner[i:i + blocksize] for i in range(0, len(inner), blocksize)] or [b""]
    blocks = []
    for ch in chunks:
        fr = xz_encode(ch)
        # store-vs-compress: compressed iff comp*16 <= unc*15 (razor-verified)
        if len(fr) * 16 <= len(ch) * 15:
            blocks.append((len(ch), fr))
        else:
            blocks.append((len(ch), ch))
    out = [struct.pack(">4sIIIIII", b"pbzx", 0, blocksize, 0, blocks[0][0], 0, len(blocks[0][1]))]
    for i, (u, payload) in enumerate(blocks):
        out.append(payload)
        if i + 1 < len(blocks):
            nu, npay = blocks[i + 1][0], len(blocks[i + 1][1])
            out.append(struct.pack(">IIII", 0, nu, 0, npay))
    return b"".join(out)


if __name__ == "__main__":
    _HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, _HERE)
    from rawenc import build_inner
    inner = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(wrap_pbzx(inner))
