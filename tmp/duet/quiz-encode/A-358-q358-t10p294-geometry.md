# A-358 (viewer r8): Q-358 T10P294 @119049 — CONFIRM all legs

First-hand bed 119049..119396 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n119049 03291000 SAME-as-P293PB0
  ✓, PB1 n119050 2b8b4e20
  SAME-as-P293C10sig ✓ (both
  byte-equal first-hand).
- PBA88-PLAIN n119051-66 16x88B
  02000000 (M8 b38,39,46,47,80-83
  16/16 distinct ✓; VPOS 9 = b4+M8
  over 88; b0 const 02, b5 const a2;
  16/16 distinct; consts 79 ✓).
- C10-1SIG n119067-76 2b8b0e23 x10
  (M13 b34,35,41-47,80-83 10/10 ✓;
  VPOS 14; b5 const a2; 10/10
  diverge; consts 70 ✓).
- QUAD88-4R n119077-140 02000000 x64
  88B-pay (VPOS 22 = b4+M8+R13 over
  88; b5 const a2 = full odd lencode
  ✓; NO frags; consts 66 ✓).
- T88-RING256 n119141-396 sig 20000000
  (VPOS 16 = b4,b5+TM6+TR8 partition
  over 0..87 ✓).
- Next P295 PB0 @119397 63501000 NEW +
  PB1 f2c7a020 NEW + PBA88 02000000
  x16 + C10-STEP 86c7a020 x10 (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad M8 b52-55,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R13 b38,39,45-51,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 db718f34…
  distinct, r123 share prefix 59064f03…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M6 [6,7,76-79] by COL 16/16; R8
  [52-55,80-83] by ROW 16/16 UNPAIRED;
  SWAPPED tail orientation first-hand
  (M carries b76-79 col, R carries
  b80-83 row); b84-87 const 668ef89f
  first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 119049..119396:
  348/348 exact.
- T88 b4 = 0xcb step2 256/256; b5 =
  0xa2+(o>=27)+(o>=155) 256/256;
  edges o26->27 (n119167->119168
  ff/a2->01/a3) + o154->155
  (n119295->119296 ff/a3->01/a4).
- Consts ALL 4 EXACT: 79/70/66/72.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
