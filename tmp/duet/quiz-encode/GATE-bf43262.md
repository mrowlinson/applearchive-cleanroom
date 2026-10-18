# GATE-bf43262 sweep: PASS-individual (rgram 2540/2540; RANGE still HELD)

- tip: lanes/encode-writer2 @bf43262 (parent 3e1e458 gated PASS). rgram
  +46/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL; novel decomposed-reuse): T10R8 n<=20216 (19961-216,
  256 cells, follows P9Q end contiguously). m=off&15 -> R8M 16 6B
  (b0,11,68-71); q=off>>4 0..15 -> FULL P9M[q] reuse decomposed: b5 =
  (P9M[q][0]+(q>=1)+(q>=9)+(q in (0,8) and m>=7))&0xFF, b6/b7 exact,
  b60-63 = P9M[q][6:] tail (AST-verified 16/16, q in-bounds).
- battery: GATE-PASS shipped legs (outdir gate-w2-bf43262-s4): RGRAM
  n=2540, PINS-RGRAM set-eq 2540/2540 (6 probes incl BOTH pre-edge
  bumps q0m7/q8m7 on FRESH oracle bytes). others green incl
  OSS/LIBCOMP/ADOPT.
- storm diligence: 4 EXTRA unpinned cells ALL CLOSED rc=0: N=19967
  (q0m6, no bump), 19977 (q1m0, +1 stair), 20095 (q8m6, no bump),
  20105 (q9m0, +2 stair) — BOTH staircase edges bracketed.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (27 descendants, all individually-closed).
- coverage: 168/169 PASS + 1 RED-held (48ebfe0).
