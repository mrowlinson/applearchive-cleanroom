# GATE-7b01d9c sweep: PASS-individual (rgram 2362/2362; RANGE still HELD)

- tip: lanes/encode-writer2 @7b01d9c (parent 028cc25 gated PASS). rgram
  +42/-0 (pure addition), for-list +5 cells, pins +10 rows append-only.
- code read (FULL, R-mirror): T10R2 n<=18128 (17873-128, 256 cells,
  follows P3Q end contiguously). m=off&15 -> R2M 16; q=off>>4 0..15 ->
  R2B5 16 + P3M[q] reuse 16 (AST-verified, q in-bounds); b5 = R2B5[q]+
  (q in (2,10) and m>=15).
- battery: GATE-PASS shipped legs (outdir gate-w2-7b01d9c-s4): RGRAM
  n=2362, PINS-RGRAM set-eq 2362/2362 (5 storm probes incl BOTH carry
  corners q2m15/q10m15 on FRESH oracle bytes). others green incl
  OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=17919
  (q2m14, below-carry), 18047 (q10m14, below-carry), 17992 (q7m7 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (15 descendants, all individually-closed).
- coverage: 156/157 PASS + 1 RED-held (48ebfe0).
