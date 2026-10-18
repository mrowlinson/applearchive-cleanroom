# NOTE-scout-r6-03: raw-vs-coded chunk rule CLOSED — 15/16 benefit line (lzfse)

## Rule (measured, oracle /usr/bin/aa macOS 27.0.1, own bytes)
Per-chunk store decision keys on COMPRESSED BENEFIT, not size:
code the chunk iff 16*c <= 15*u (coded saves at least 1/16 =
6.25%), else store RAW (payload = raw bytes, c == u, no magic).
Applies to EVERY chunk (first/full/tail, -b 1k + 4k anchors),
position- and block-size-independent.

## Evidence (NVME r6/rawfloor/, -a lzfse -t 1, end==size all,
zero ANOMALY cells; discriminator: bvxn/bvx2 magic = coded,
c==u non-magic = RAW)
- phrase tails u=1..260 step 1 (260 cells): RAW 1..101,
  coded 102..260 (c=95 const). Step 101|102: 16*95=1520 vs
  15*101=1515 (raw side) / 15*102=1530 (coded side). EXACT.
- zeros tails u=51..100 + anchors (53 cells): RAW ..71,
  coded 72.. (c=67 const). Step 71|72: 16*67=1072 vs
  15*71=1065 / 15*72=1080. EXACT.
- cycle256 tails u=1..520 step 1 (520 cells): RAW 1..345,
  coded 346..520 (c=324 const, one 323 wobble at u=352 away
  from step). Step 345|346: 16*324=5184 vs 15*345=5175 /
  15*346=5190. EXACT modulo const-c at u=345 (run 346-351
  all 324 supports it).
- random (incompressible): tails u=50/101/102/200 + full-1024
  chunks ALL RAW (c==u; first-chunk payload starts AA01 —
  raw stream bytes). Benefit rule active at all sizes.
- Excluded: fixed floor (steps at 72/102/346 move with
  content); pure benefit c<u (phrase u=101 saves ~6 yet RAW);
  absolute margin (zeros codes saving 5, phrase raw saving 6);
  wrapper-excluded compare; ratios 7/8 and 31/32. Threshold
  interval from 3/3 boundary hits is [0.9364,0.939); 15/16 =
  0.9375 is the unique simple fraction (single-shift compare).

## Stream-layout incidental (supports const-c runs)
Tail content = fixed prefix + end extension (RAW prefixes
constant across N: phrase 'ick '.., zeros 0000.., cycle
56f13aaa..), i.e. headers + N data bytes + ~44B meta footer.
Coded c const over long u runs because extension bytes are
perfect matches. Decoder rule unchanged: magic-sniff per
chunk, accept both.

## Container-lane consequence
- Encoder-side: per chunk, code iff the coded payload beats
  15/16 of u, else emit raw — REQUIRED for oracle-identical
  bytes. Doc pin queued (FIXTURES §4 bullet, this run).
- Unprobed (follow-up, cheap): other codecs' chunk magics +
  whether their benefit lines match 15/16 (script takes
  codec=; per-codec payload magics unknown — lzma/lz4/lzraven/
  zlib/lzbitmap chunk-magic census first).
- Inbox (round 5): 364 Q, zero scout-directed, DONE unchanged,
  no wall/kickoff/donor traffic.
