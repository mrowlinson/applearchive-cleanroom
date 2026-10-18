# GATE-b95eaa4 sweep: PASS-individual (rgram 2422/2422; RANGE still HELD)

- tip: lanes/encode-writer2 @b95eaa4 (parent 8910f7f gated PASS). rgram
  +44/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL, R-mirror): T10R4 n<=18824 (18569-824, 256 cells,
  follows P5Q end contiguously). m=off&15 -> R4M 16; q=off>>4 0..15 ->
  R4B5 16 + P5M[q] reuse 16 (AST-verified, q in-bounds); b5 = R4B5[q]+
  (q in (7,15) and m>=7).
- battery: GATE-PASS shipped legs (outdir gate-w2-b95eaa4-s4): RGRAM
  n=2422, PINS-RGRAM set-eq 2422/2422 (6 storm probes BRACKET both
  carry edges: q7m0/m7 + q15m0/m7, on FRESH oracle bytes). others green
  incl OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=18687
  (q7m6, below-carry), 18815 (q15m6, below-carry), 18629 (q3m12 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (19 descendants, all individually-closed).
- coverage: 160/161 PASS + 1 RED-held (48ebfe0).
