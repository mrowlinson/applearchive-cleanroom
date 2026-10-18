# GATE-bb9c6c6 sweep: PASS-individual (rgram 2438/2438; RANGE still HELD)

- tip: lanes/encode-writer2 @bb9c6c6 (parent b95eaa4 gated PASS). rgram
  +161/-0 (pure addition), for-list +8 cells, pins +16 rows append-only.
- code read (ALL 5 branches; NO-DIP head variant): P60 singleton
  (18825, b0=01, follows R4 end contiguously) + P61 singleton (18826,
  b0=80) + P6A 16-row (18827-42, off0-15, P6A 16) + P6B 10-row
  (18843-52, off0-9, P6B 10) + P6Q 4x16 (18853-916: m0-15 P6M 16,
  q0-3 P6Q 4; b5 = CONST 0x13, no carry — corner-only P6Q probes
  adequate). AST-verified all rows + offsets.
- battery: GATE-PASS shipped legs (outdir gate-w2-bb9c6c6-s4): RGRAM
  n=2438, PINS-RGRAM set-eq 2438/2438; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- quad diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=18874
  (q1m5), 18896 (q2m11), 18904 (q3m3) — all 4 quartets now sampled.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (20 descendants, all individually-closed).
- coverage: 161/162 PASS + 1 RED-held (48ebfe0).
