# GATE-32a89ff sweep: PASS-individual (rgram 2392/2392; RANGE still HELD)

- tip: lanes/encode-writer2 @32a89ff (parent efc8f69 gated PASS). rgram
  +44/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL, R/R2-mirror): T10R3 n<=18476 (18221-476, 256 cells,
  follows P4Q end contiguously). m=off&15 -> R3M 16; q=off>>4 0..15 ->
  R3B5 16 + P4M[q] reuse 16 (AST-verified, q in-bounds); b5 = R3B5[q]+
  (q in (5,13) and m>=3).
- battery: GATE-PASS shipped legs (outdir gate-w2-32a89ff-s4): RGRAM
  n=2392, PINS-RGRAM set-eq 2392/2392 (6 storm probes BRACKET both
  carry edges: q5m0/m3 + q13m0/m3, on FRESH oracle bytes). others green
  incl OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=18303
  (q5m2, below-carry), 18431 (q13m2, below-carry), 18374 (q9m9 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (17 descendants, all individually-closed).
- coverage: 158/159 PASS + 1 RED-held (48ebfe0).
