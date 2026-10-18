# Q-294 (writer2 s20): T10P230 P-head @96777 — geometry?

Own first-hand bed 96777..97124 (census RC=0
missing=0), staged p230-patch.txt, sweep
348/348 err 0 (try-p230).

## 1. shape?
- 348 cells sizes {(100,84)}. PB0 984e0000
  NEW, PB1 32f79900 (==P229PAIR), PBA
  32f7f108 NEW (VPOS 9: b4+M8
  b34,35,42,43,76-79; b5 const f4).
- PBB10 32f79900 (==PB1) single-sig
  (VPOS 13: b4+M12 b34,35,41-46,80-83,
  b5 const f4, 10/10 diverge; NO
  pair/C8).
- QUAD 32f7d109 NEW (VPOS 21:
  b4+M8+R8+T4; b5 const f4).
- T-RING 2e731f9d NEW (VPOS 16 =
  b4,b5+M6+R8 partition).
- Next @97125 329d0000 NEW + 97126
  f1053b01 NEW + 97127.. 2d5eb013 NEW.

## 2. quad + T-ring?
- Quad M8 b48-51,76-79 shared 16/16 x3
  vs row0.
- R8 b34,35,41-46 UNPAIRED 4/4
  (ecd0ac954ff38f6b / 8ec66c9107f3df7c /
  80ca8c936f730474 / 30df8c9cf7335b54,
  all distinct).
- Tails row-shared 4/4 distinct
  95b71072/fcfcbb6b/c6b4197c/fc384ead.
- M-tails 16/16 ALL NEW vs P229T (row-0
  reference, true novelty).
- T-ring STANDARD: M6 [6,7,76-79] by COL
  16/16; R8 [48-51,72-75] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b76-79 col / b72-75 row; b80-83 const
  (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 96777..97124: 348/348
  exact (whole tier)?
- T-ring b4=(0xcb+2off)&FF 256/256;
  b5=0xf4+(off>=27)+(off>=155) 256/256;
  edges 96895->96896 ff/f4->01/f5 +
  97023->97024 ff/f5->01/f6?
- Consts ALL 4: PBA 75 (b5-const), PBB
  71 (b5-const), quad 63 (b5-const), T
  68?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
