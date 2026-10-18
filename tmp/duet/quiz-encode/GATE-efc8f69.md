# GATE-efc8f69 sweep: PASS-individual (rgram 2380/2380; RANGE still HELD)

- tip: lanes/encode-writer2 @efc8f69 (parent 7b01d9c gated PASS). rgram
  +162/-0 (pure addition), for-list +9 cells, pins +18 rows append-only.
- code read (ALL 5 branches, P2/P3-mirror + q-b5-tab twist): D29
  singleton 68B dip (18129, follows R2 end contiguously) + P40 singleton
  (18130) + P4A 16-row (18131-46, off0-15, P4A 16) + P4B 10-row
  (18147-56, off0-9, P4B 10) + P4Q 4x16 (18157-220: m0-15 P4M 16, q0-3
  P4Q 4 + P4B5 4; b5 = P4B5[q]+(q==1 and m>=3)). AST-verified all
  rows + offsets. pinned probe 18176 = off19 = q1m3 EXACT carry edge.
- battery: GATE-PASS shipped legs (outdir gate-w2-efc8f69-s4): RGRAM
  n=2380, PINS-RGRAM set-eq 2380/2380; all other legs green incl
  OSS/LIBCOMP/ADOPT.
- quad diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=18175
  (q1m2, below-carry), 18198 (q2m9), 18205 (q3m0).
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (16 descendants, all individually-closed).
- coverage: 157/158 PASS + 1 RED-held (48ebfe0).
