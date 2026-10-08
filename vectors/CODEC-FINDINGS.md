# Codec findings (encode-writer1, black-box oracle I/O only, macOS 27.0.1)

Outer wrapper shared: pbz+tag, 12B prefix (magic, u32 0, u32BE blocksize)
+ per-block 16B hdr (0, unc BE, 0, comp BE) + payload; non-last blocks
chained; store rule per block: compressed iff comp*16 <= unc*15.

| alg | magic | payload | byte-exact via | status |
| raw | AA01 (none) | inner | own impl | DONE (11/11) |
| lzfse | pbze | lzfse frame (bvx2..bvx$) | OSS lzfse/lzfse (BSD) | DONE (4/4) |
| zlib | pbzz | raw zlib stream | stock zlib level 5 | DONE (4/4) |
| lzma | pbzx | xz stream, check NONE, LZMA2 dict 8M lc3lp0pb2 | stock liblzma preset-6 packets (5.8.4 pin) + own XZ framing rewrite | DONE (6/6 + holdout 12/12; A-20 grant; razor +15/-135) |
| lz4 | pbz4 | Apple frame bv41+u32le unc+u32le len+lz4 block+bv4$ | — | PARKED: 26 OSS settings fail (default/HC/fast); Apple matchfinder differs |
| lzbitmap | pbzb | ZBM stream | — | PARKED: Corellium libzbitmap bytes differ (242 vs 272) |
| lzraven | pbzm | unknown (2b 00 ca ec..) | — | OPEN, viewer Q-9(a) |

zlib level proof: 10/10 discriminating trials L5-ONLY (L4 differs, oracle==L5).
lzma notes: packet bytes = stock liblzma preset-6 (12/12 beds + full-file
5/5); XZ block/index/footer = Apple-custom, rewritten in src/lzmaenc.py (b0 =
4 iff unc>=2^21 else 3, flags 0xC0, bcs/unpadded EXCL lzma2 pad, footer
crc(back+flags), backward=(idxlen-4)/4). prior 355-combo fail compared full
payloads incl framing (A-10(b) refined per A-20). pin: FORMAT raw-LZMA1
preset-6 + VERSION 5.8.4 (/opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib
sha256 1b2e12cc...) + battery.
lz4 notes: payload IS a valid lz4 block (literals+matches visible); Apple
block 317B vs OSS best 200B — a worse/faster matchfinder, no OSS knob hits it.
