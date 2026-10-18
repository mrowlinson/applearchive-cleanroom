# GATE-adc7178 sweep: PASS-individual (rgram 2480/2480; RANGE still HELD)

- tip: lanes/encode-writer2 @adc7178 (parent fedc0db gated PASS). rgram
  +52/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL; richest storm yet): T10R6 n<=19520 (19265-520, 256
  cells, follows P7Q end contiguously). m=off&15 -> R6M 16 (b20-22,
  64-67); q=off>>4 0..15 -> R6B5 16 + R6B17 16 + R6B18 16 + P7M[q][6:]
  tail-4B reuse (AST-verified all 16, q in-bounds); b5 = R6B5[q]+
  (q in (3,11) and m>=15).
- battery: GATE-PASS shipped legs (outdir gate-w2-adc7178-s4): RGRAM
  n=2480, PINS-RGRAM set-eq 2480/2480 (6 probes incl BOTH carry
  corners q3m15/q11m15 on FRESH oracle bytes). others green incl
  OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=19327
  (q3m14, below-carry), 19455 (q11m14, below-carry), 19400 (q8m7 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (23 descendants, all individually-closed).
- coverage: 164/165 PASS + 1 RED-held (48ebfe0).
