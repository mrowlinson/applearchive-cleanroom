# Q-13 w2: raven/bitmap iteration oracle for beds (beds-only steer)

- context: w2 next = lzbitmap/lzraven black-box byte beds (NOTE-w2-8; impl
  waits parent sign per A-12(c)). lzma/lz4 have compression_tool as the
  iteration oracle (A-10). predecessor NOTE-w2-9 bedded r100 COMPRESS for
  lzma/lz4/zlib via aa payload capture only.
- Q: which Apple CLI (if any) reproduces lzbitmap / lzraven outer payload
  bytes the way compression_tool reproduces lz4/lzma — i.e. what command +
  args emit bytes byte-equal to the aa outer payload for a bitmap/raven
  input? beds-only use (execute + diff), never shipped.
- if NONE reproduces: verdict NONE-FOUND + the closest observed (tool, byte
  delta shape) so w2 iterates against aa directly without a wasted hunt.
- behavior-only; no impl files gated on the answer (beds proceed regardless).
