# GATE-1ceaac9 sweep: PASS-individual (rgram 2336/2336; RANGE still HELD)

- tip: lanes/encode-writer2 @1ceaac9 (parent 9f63083 gated PASS). rgram
  +42/-0 (pure addition), for-list +5 cells, pins +10 rows append-only.
- code read (FULL): T10R n<=17780 (17525-780, 256 cells, follows P2Q end
  contiguously). m=off&15 -> RM 16; q=off>>4 0..15 -> RB5 16 + P2M[q]
  reuse 16 (AST-verified, q in-bounds everywhere); b5 = RB5[q]+(q in
  (0,8) and m>=11).
- battery: GATE-PASS shipped legs (outdir gate-w2-1ceaac9-s4): RGRAM
  n=2336, PINS-RGRAM set-eq 2336/2336 (5 storm probes incl BOTH carry
  boundaries q0m11/q8m11 on FRESH oracle bytes). others green incl
  OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=17535
  (q0m10, below-carry), 17665 (q8m12, above-carry), 17610 (q5m5 mid).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (13 descendants, all individually-closed).
- coverage: 154/155 PASS + 1 RED-held (48ebfe0).
