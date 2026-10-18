# GATE-ec3080a sweep: PASS-individual (rgram 2500/2500; RANGE still HELD)

- tip: lanes/encode-writer2 @ec3080a (parent adc7178 gated PASS). rgram
  +168/-0 (pure addition), for-list +10 cells, pins +20 rows append-
  only.
- code read (ALL 5 branches; no-dip head + 2-step b5): P80 singleton
  (19521, b0=10, follows R6 end contiguously) + P81 singleton (19522,
  b0=28) + P8A 16-row (19523-38, off0-15, P8A 16) + P8B 10-row
  (19539-48, off0-9, P8B 10) + P8Q 4x16 (19549-612: m0-15 P8M 16 7B,
  q0-3 P8Q 4 8B; b5 = 0x98+(q==3)+(q==2 and m>=3)). AST-verified all
  rows + offsets. pinned 19584 = q2m3 EXACT edge + 19597/19612 span
  q3.
- battery: GATE-PASS shipped legs (outdir gate-w2-ec3080a-s4): RGRAM
  n=2500, PINS-RGRAM set-eq 2500/2500; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- quad diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=19583
  (q2m2, below-edge), 19574 (q1m9), 19604 (q3m7) — all 4 quartets now
  sampled.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (24 descendants, all individually-closed).
- coverage: 165/166 PASS + 1 RED-held (48ebfe0).
