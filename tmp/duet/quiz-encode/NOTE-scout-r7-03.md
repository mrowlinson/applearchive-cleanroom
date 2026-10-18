# NOTE-scout-r7-03: per-codec raw-vs-coded rules CLOSED (all 6 codecs)

## Census (24 cells, NVME r7/census/, oracle /usr/bin/aa macOS 27.0.1)
Same pbz* framing every codec (z0==0, per-chunk z1/u/z2/c).
Stream magics: lzfse pbze, lzma pbzx, lz4 pbz4, lzraven pbzm,
zlib pbzz, lzbitmap pbzb. Payload magics: bvxn / xz fd377a58 /
bv41 (NEW, was not in r6's set) / 2b00caec / zlib 78.. / ZBM\t
(5a424d09). Uncompressed stream layout codec-independent
(N=100->u344, N=2000->1024+1024+196 all codecs).

## Benefit rules (~455 sweep cells, NVME r7/benefit/, zero ANOMALY)
- lzma: 15/16 EXACT. Step 140|141 (c=132 const): 16*132=2112
  vs 15*140=2100 (raw) / 15*141=2115 (coded). 4k anchor identical.
- lzraven: 15/16 EXACT. Step 98|99 (c=92 const): 1472 vs
  1470/1485. 4k anchor identical.
- zlib: 15/16 EXACT. Step 78|79 (c=74 const): 1184 vs 1170/1185.
  4k anchor identical.
- lz4: 15/16 on ACTUAL per-u c. c(u) wobbles (+1/u runs, wraps
  ~7: phrase 171..178, zeros 144..151, cyc 400..407), so steps
  near-miss const-c prediction by 1-4B (183|184, 157|158,
  428|429). No single const-c ratio fits all three (phrase band
  (0.929,0.934] vs zeros band (0.911,0.917] disjoint); no single
  margin (13/14/29). Step positions match 15/16 (any-benefit
  would sit at c~=u: ~175/~147/~403 — all refuted). All coded
  cells hug 0.991+. 4k: IDENTICAL step + c values (c is pure
  function of tail-u). Residual: raw-side hypothetical c
  unobservable by construction (black-box limit, same kind as
  r6's const-c inference).
- lzbitmap: floor u>=145 AND 15/16 benefit. Floor: exact step
  144|145 in 3/3 draws with different c (phrase c=116, zeros
  c=90, 4k phrase c=119) — no ratio/margin does that.
  Benefit half: random tails/fulls above floor all RAW;
  mixed-0.68 flip codes at c/u=159/170, 16*159=2544 vs
  15*170=2550 (margin 6, hugs 15/16); 7/8 excluded (coded at
  0.9176). Rule: code iff u>=145 AND 16*c<=15*u.
- Random (all 5 codecs): every chunk RAW incl. full-1024s and
  the u=196 tail; first-chunk payload starts AA01 (raw stream
  bytes, matches r6).

## Container-lane consequence
- Encoder-side per-chunk rule is now COMPLETE for all codecs:
  shared 15/16 comparator on actual (u,c); lzbitmap adds a
  u>=145 floor; lz4 needs no special-casing (compare actual c).
  REQUIRED for oracle-identical bytes. Doc pin queued (this run).
- r6-03 follow-up FULLY CLOSED. No further solo benefit work.
