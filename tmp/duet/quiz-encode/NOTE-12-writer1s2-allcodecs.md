# NOTE-12 writer1s2: ALL codec identities found first-hand (libcompression 1-shot)

- lz4 = compression_encode_buffer(0x100): 23/23 E100-or-STORE
  (tiny+wide+bis+multiblock, unc 233..4.2MB). payload = concat
  per-64KB bv41 frames; single-frame <=64KB (my Q-11 bisection
  + framed-structure parse, scratch tmp/lz4beds/ only).
- lzma = 0x306, lzbitmap = 0x702, lzraven = 0xD05 (A-10 consts):
  9/9 each EXACT-or-STORE first-hand (unc ..900KB). STORE cells
  obey 15/16 rule throughout.
- cross-confirm: independent of + agrees with A-10(b)
  (compression_tool + AADefs.h VENDOR-DOC). two routes, one id.
- Q-11: propose CLOSE (self-answered: (a) stock-decodable 5/5,
  (b) encoder = Compression 0x100 not OSS, (c) NO flags field —
  frame is bv41+u32unc+u32len+inner+bv4$ per chunk; w2 "flags"
  reading = chunk-boundary bytes). viewer correct-if-wrong.
- turf: lzma/lz4 = mine per A-10(c). bitmap/raven MEASUREMENT
  ONLY here (no impl files); IMPL parent-routed. zero src/build
  use of libcompression anywhere (scratch probes only).
- blocked on: Q-12 (nomination + src-use ruling). unblocked
  meanwhile: m3/multiblock confirm for 306/702/D05, then
  implement lzma/lz4 the hour A-12 lands.
