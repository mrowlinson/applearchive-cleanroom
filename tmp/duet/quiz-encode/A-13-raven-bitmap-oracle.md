# A-13 raven/bitmap iteration oracles: raven=YES (2 paths), bitmap=libcompression-only (MEASURED)

## raven: compression_tool reproduces aa outer payload EXACT
- bed (own, WS scratch-viewer3/bed.py, inner 1109B fixed): aa -a lzraven block payload 504B ==
  compression_tool -encode -a lzraven(inner) EXACT (IDENTICAL=True). same class as A-10 lzma/lz4.
- second path: libcompression COMPRESSION_LZRAVEN (0xD05) buffer call == same 504B payload EXACT.
- steer: iterate raven against compression_tool exactly like lzma/lz4. beds-OK, never shipped (A-9/A-10 class).

## bitmap: compression_tool REJECTS; libcompression reproduces EXACT
- compression_tool -encode -a lzbitmap -> rc=1 usage error; -A lzbitmap -> rc=1 same. algo list is
  zlib/lzma/lzraven/lzfse/lz4/lz4_raw only (own -h read). verdict for compression_tool: NONE-FOUND.
- BUT libcompression COMPRESSION_LZBITMAP (0x702, buffer API, macOS 12+) == aa -a lzbitmap block
  payload 538B EXACT (own ctypes bed, IDENTICAL=True). same beds-OK class as A-12(a) lzma/lz4 one-shots.
- VENDOR-DOC (compression.h, CLT 27.0 SDK, own grep): LZBITMAP=0x702 "buffer API only"; LZRAVEN=0xD05
  "buffer API only, macOS 27.0+". public constants, documented call shape — behavior use only.
- steer: iterate bitmap against libcompression one-shot (beds-only, same provenance rule as A-12:
  shared-cache resident, pin OS build 26A434 per bed, re-pin on bump). no wasted hunt needed.

## scope
- both oracles cover the COMPRESS path (codec bytes for a block input). STORE path needs no oracle
  (payload = raw slice, w2 NOTE-w2s2-6). 15/16 decision stays aa-measured (A-6(f) + NOTE-w2s2-8).
