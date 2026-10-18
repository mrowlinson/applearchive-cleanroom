# A-300 (viewer r3): Q-294 T10P230 P-head @96777 — CONFIRM + 3 const fixes

First-hand bed 96777..97128 (q294.py new;
census 96097..97124 + 97125..97140 RC=0
missing=0).

## 1. shape: CONFIRM + PBB VPOS fix
- 348 cells sizes {(100,84)}. PB0 984e0000
  NEW, PB1 32f79900 (==P229PAIR), PBA
  32f7f108 NEW (VPOS 9 exact b4+M8
  b34,35,42,43,76-79, b5 const f4).
- PBB10 32f79900 (==PB1) single-sig.
  CORRECTION: VPOS 13 (not 14) = b4+M12
  (not M13) — listed positions
  b34,35,41-46,80-83 are exact (12 + b4
  = 13); name/count wrong. Consts 71
  (not 70). b5 const f4, 10/10 diverge;
  NO pair/C8.
- QUAD 32f7d109 NEW (VPOS 21 exact ex-b5:
  b4+M8+R8+T4 = 1+8+8+4; b5 const f4
  single-valued — "b4,b5+" prefix loose,
  sums 22).
- T-RING 2e731f9d NEW (VPOS 16 exact =
  b4,b5+M6+R8 partition).
- Next @97125 329d0000 NEW + 97126
  f1053b01 NEW + 97127/28 2d5eb013 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M8 b48-51,76-79 shared 16/16 x3 vs
  row0.
- R8 b34,35,41-46 UNPAIRED 4/4 EXACT
  values (ecd0ac954ff38f6b/8ec66c9107f3df7c/
  80ca8c936f730474/30df8c9cf7335b54, all
  distinct).
- Tails row-shared 4/4 distinct
  95b71072/fcfcbb6b/c6b4197c/fc384ead
  EXACT.
- M-tails 16/16 ALL NEW vs P229T (row-0
  reference, true novelty).
- T-ring STANDARD: M6 [6,7,76-79] by COL
  16/16; R8 [48-51,72-75] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b76-79 col-shared (M-role ✓ by passing
  col check) / b72-75 row-shared (R-role
  ✓ by passing row check); b80-83 const
  (1 ring-wide ✓).

## 3. counters + dips: CONFIRM + 3 const fixes
- Odd-lencode ALL 96777..97124: 348/348
  exact (whole tier).
- T-ring b4=(0xcb+2off)&FF 256/256;
  b5=0xf4+(off>=27)+(off>=155) 256/256;
  edges 96895->96896 ff/f4->01/f5 +
  97023->97024 ff/f5->01/f6.
- CORRECTIONS: PBA consts 75 (not 74;
  VPOS 9); PBB consts 71 (not 70; VPOS
  13); quad consts 63 (not 62; VPOS 21).
  (7 head-group off-by-ones now: filed =
  84-VPOS-1 in Q-292 PBA/PBC, Q-293
  PBA/PBC, Q-294 PBA/PBB/quad — analyzer
  consts systematically 1 low on head
  groups.) T 68 ✓.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; PBA 75 + PBB V13/C71 + quad 63
