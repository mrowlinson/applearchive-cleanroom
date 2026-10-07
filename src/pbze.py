#!/usr/bin/env python3
"""pbze outer wrapper. Derived black-box from /usr/bin/aa I/O only.
Blocks: inner split by blocksize; per block lzfse-frame iff comp<unc
else raw; non-last blocks += 16B BE(0,next_unc,0,next_comp).
"""
import ctypes
import os
import struct
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_DYLIB = os.environ.get("LZFSE_DYLIB", "/Volumes/NVME/applearchive-cleanroom-ws/tools/lzfse/build/bin/liblzfse.dylib")

_lib = None


def _liblzfse():
    global _lib
    if _lib is None:
        _lib = ctypes.CDLL(_DYLIB)
        _lib.lzfse_encode_buffer.argtypes = [ctypes.c_char_p, ctypes.c_size_t,
                                             ctypes.c_char_p, ctypes.c_size_t, ctypes.c_void_p]
        _lib.lzfse_encode_buffer.restype = ctypes.c_size_t
    return _lib


def lzfse_encode(chunk):
    lib = _liblzfse()
    dst = ctypes.create_string_buffer(len(chunk) + 4096)
    n = lib.lzfse_encode_buffer(dst, len(dst), chunk, len(chunk), None)
    if n == 0:
        return None
    return dst.raw[:n]


def wrap_pbze(inner, magic=b"pbze", blocksize=4 * 1024 * 1024):
    chunks = [inner[i:i + blocksize] for i in range(0, len(inner), blocksize)] or [b""]
    blocks = []
    for ch in chunks:
        fr = lzfse_encode(ch) if magic == b"pbze" else None
        # store-vs-compress: compressed iff comp*16 <= unc*15 (100/100 probes)
        if fr is not None and len(fr) * 16 <= len(ch) * 15:
            blocks.append((len(ch), fr))
        else:
            blocks.append((len(ch), ch))
    out = [struct.pack(">4sIIIIII", magic, 0, blocksize, 0, blocks[0][0], 0, len(blocks[0][1]))]
    for i, (u, payload) in enumerate(blocks):
        out.append(payload)
        if i + 1 < len(blocks):
            nu, npay = blocks[i + 1][0], len(blocks[i + 1][1])
            out.append(struct.pack(">IIII", 0, nu, 0, npay))
    return b"".join(out)


if __name__ == "__main__":
    sys.path.insert(0, _HERE)
    from rawenc import build_inner
    inner = build_inner(os.fsencode(sys.argv[1]))
    with open(sys.argv[2], "wb") as f:
        f.write(wrap_pbze(inner))
