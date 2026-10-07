# Codec findings (encode-writer1, black-box oracle I/O only, macOS 27.0.1)

Outer wrapper shared: pbz+tag, 12B prefix (magic, u32 0, u32BE blocksize)
+ per-block 16B hdr (0, unc BE, 0, comp BE) + payload; non-last blocks
chained; store rule per block: compressed iff comp*16 <= unc*15.

| alg | magic | payload | byte-exact via | status |
| raw | AA01 (none) | inner | own impl | DONE (11/11) |
| lzfse | pbze | lzfse frame (bvx2..bvx$) | OSS lzfse/lzfse (BSD) | DONE (4/4) |
| zlib | pbzz | raw zlib stream | stock zlib level 5 | DONE (4/4) |
| lzma | pbzx | xz stream, check NONE, LZMA2 dict 8M lc3lp0pb2 | — | PARKED: 355 liblzma setting combos fail; Apple-internal encoder |
| lz4 | pbz4 | Apple frame bv41+u32le unc+u32le len+lz4 block+bv4$ | — | PARKED: 26 OSS settings fail (default/HC/fast); Apple matchfinder differs |
| lzbitmap | pbzb | ZBM stream | — | PARKED: Corellium libzbitmap bytes differ (242 vs 272) |
| lzraven | pbzm | unknown (2b 00 ca ec..) | — | OPEN, viewer Q-9(a) |

zlib level proof: 10/10 discriminating trials L5-ONLY (L4 differs, oracle==L5).
lzma notes: xz container parses (stream flags NONE, 1 filter LZMA2 0x21,
props 0x16=8MB, lzma props 0x5d=lc3lp0pb2); grid over mode/mf/nice_len/depth/
dict/extreme all fail; Apple beats liblzma here (236 vs 240).
lz4 notes: payload IS a valid lz4 block (literals+matches visible); Apple
block 317B vs OSS best 200B — a worse/faster matchfinder, no OSS knob hits it.
