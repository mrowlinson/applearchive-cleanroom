# GATE-141e67e sweep: PASS-individual (rgram 2512/2512; RANGE still HELD)

- tip: lanes/encode-writer2 @141e67e (parent ec3080a gated PASS). rgram
  +42/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL, R-mirror): T10R7 n<=19868 (19613-868, 256 cells,
  follows P8Q end contiguously). m=off&15 -> R7M 16; q=off>>4 0..15 ->
  R7B5 16 + P8M[q] reuse 16 (AST-verified, q in-bounds); b5 = R7B5[q]+
  (q in (6,14) and m>=3).
- battery: GATE-PASS shipped legs (outdir gate-w2-141e67e-s4): RGRAM
  n=2512, PINS-RGRAM set-eq 2512/2512 (6 storm probes BRACKET both
  carry edges: q6m0/m3 + q14m0/m3, on FRESH oracle bytes). others green
  incl OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=19711
  (q6m2, below-carry), 19839 (q14m2, below-carry), 19783 (q10m10 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (25 descendants, all individually-closed).
- coverage: 166/167 PASS + 1 RED-held (48ebfe0).
