# A-359 (viewer r8): Q-359 T10P295 @119397 — CONFIRM all legs

First-hand bed 119397..119744 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n119397 63501000 NEW, PB1 n119398
  f2c7a020 NEW.
- PBA88-PLAIN n119399-414 16x88B
  02000000 (M7 b13,14,15,80-83 16/16
  distinct ✓; VPOS 8 = b4+M7 over 88;
  b0 const 02, b5 const a4; 16/16
  distinct; consts 80 ✓).
- C10-STEP n119415-24 86c7a020 x10
  1-sig (M11 b13-19,80-83 10/10 ✓;
  VPOS 13 = b4,b5+M11; b5 0xa4+(o>=9),
  edge o8->9 n119423->119424
  ff/a4->01/a5 ✓; 10/10 diverge;
  consts 71 ✓).
- QUAD88-4R-FRAG n119425-488 02000000
  x64 88B-pay (VPOS 21 = b4+M8+R11+F1
  over 88; b5 const a5 = full odd
  lencode ✓; consts 67 ✓).
- T88-RING256 n119489-744 sig 20000000
  (VPOS 16 = b4,b5+TM6+TR8 partition
  over 0..87 ✓).
- Next P296 PB0 @119745 63501000
  (==P295PB0) + PB1 7b80af20 NEW +
  PBA88 02000000 x16 + C10 7b80af20
  (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M8 b16-19,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R11 b8-11,20,21,22,84-87 rows
  4/4 NO pairing EXACT first-hand (4
  distinct row-tuples; r0 d9183f31…
  distinct, r123 share prefix 99365f3c…
  but differ in tail bytes).
- FRAG b23 coltab+ADD1 EXACT
  first-hand: r123 == r0+1 (mod 256)
  48/48 (r0-row tab + 3 derived rows).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M6 [28,29,80-83] by COL 16/16;
  R8 [20-23,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row (standard); b84-87 const
  21e74240 first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 119397..119744:
  348/348 exact.
- T88 b4 = 0x83 step2 256/256; b5 =
  0xa5+(o>=63)+(o>=191) 256/256;
  edges o62->63 (n119551->119552
  ff/a5->01/a6) + o190->191
  (n119679->119680 ff/a6->01/a7).
- Consts ALL 4 EXACT: 80/71/67/72.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
