# NOTE-scout-r2-06: pbz* outer container — DERIVED SPEC (black-box)

## Model (proven byte-exact, macOS 27.0.1; all six codecs uniform)
An `-a <codec>` archive = 12B outer header + N chunk records wrapping
the whole AA01 entry stream (NOT per-DAT framing — r1 NOTE-03's
"DAT blobs carry framing" is SUPERSEDED):
- 0-3: magic pbz4/pbzb/pbze/pbzx/pbzm/pbzz (FIXTURES §4 reconfirmed)
- 4-7: u32 0
- 8-11: BE u32 -b block size (1024/16384/65536/1048576/4194304 all
  observed matching the -b flag; L5 default pins show 4194304)
- per chunk (16B header + payload, chunk0 header starts at 12):
  BE u32 0, BE u32 uncomp-len, BE u32 0, BE u32 comp-len, then
  comp-len payload bytes. Concat of decoded payloads = raw AA01
  stream byte-for-byte.

## Proofs (independent oracle tools, own bytes only)
- Single-chunk: bytes[28:28+comp] via `compression_tool -decode`
  == raw stream EXACT for lzfse (@28 MATCH), lzma, lz4
  (via -a lz4; -a lz4_raw FAILS — disambiguated), lzraven.
- Multi-chunk: -b 1k over 900530B stream = 880 chunks walked, every
  header (0,u,0,c), end offset == file size exactly,
  concat == raw stream (MULTICHUNK-CONCAT-MATCH).
- Payload magics: lzfse bvxn/bvx2, lzma FD377A585A00 (XZ container,
  matches man), zlib 78 5E, lz4 `bv41`, lzraven 2B00CAEC...,
  lzbitmap `ZBM`.
- Nuances: (a) zlib chunks are zlib-WRAPPED deflate (python
  zlib.decompress MATCH; tool emits RAW deflate per man — chunk !=
  tool framing here; only exception). (b) lzfse v1/v2 per chunk:
  1k chunks v1, >=4k-full v2, short TAIL chunk v1 (threshold in
  (2445,4096], selector trivia OPEN — decoder rule firm: accept
  both magics per chunk). (c) lzbitmap has NO compression_tool
  path (absent from -a list) — chunk decode needs aa convert or
  decode-side work. (d) -b 1m vs 4m on sub-1m input: identical
  except header block-size field.

## Container-lane consequences
- Framing split is now three layers: pbz* chunk walk -> AA01 header
  chain (NOTE-06 r1: 82/98/99, header+parsed-blob stepping) ->
  field parse. -b selects chunking only; -a selects chunk codec.
- T2 -b sweep already half-measured here (b1k/b4k/b8k/b16k/b64k/
  b1m/b4m on 900KB); T2 corpus should PIN the -b sweep cells +
  threshold notes. lzbitmap + zlib-wrap are the two special cases.
