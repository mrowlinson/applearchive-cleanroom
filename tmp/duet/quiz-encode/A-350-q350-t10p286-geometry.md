# A-350 (viewer r8): Q-350 T10P286 @116265 — CONFIRM all legs

First-hand bed 116265..116612 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n116265 1df80a00 NEW, PB1 n116266
  cd23fd15 SAME-as-P285C10sig ✓
  (byte-equal to n115935 first-hand).
- PBA88-PLAIN n116267-82 16x88B
  01000000 (M positions b38,46,47,
  80-83 16/16 distinct ✓; VPOS 8 =
  b4 + those 7 over 88; b0 const 01,
  b5 const 8c; 16/16 distinct; consts
  80 ✓; NOTE: staged label says "M6"
  but names 7 varying positions — all
  7 vary first-hand and consts math
  uses vpos 8, so geometry stands as
  staged, label nit only).
- C10-1SIG n116283-92 cd236d10 x10
  (M13 b34,35,41-47,80-83 10/10 ✓;
  VPOS 14; b5 const 8c; 10/10
  diverge; consts 70 ✓).
- QUAD88-4R n116293-356 01000000 x64
  88B-pay (VPOS 22 = b4,b5+M9+R11
  over 88; b5 0x8c+(o>=59), edge
  o58->59 n116351->116352 ff/8c->
  01/8d ✓; NO frags; consts 66 ✓).
- T88-RING256 n116357-612 sig 10000000
  (VPOS 19 = b4,b5+TM8+TR9 partition
  over 0..87 ✓).
- Next P287 PB0 @116613 85620b00 NEW +
  PB1 4c0ac516 NEW + PBA88 01000000
  x16 + C10 86148a2d (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M9 b51-55,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R11 b38,39,46-50,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 8549271f…
  distinct, r123 share 11B-prefix
  fb421acf3422 but differ in tail
  bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [6,7,12,13,76-79] by COL
  16/16; R9 [51-55,80-83] by ROW 16/16
  UNPAIRED; SWAPPED tail orientation
  first-hand (M carries b76-79 col, R
  carries b80-83 row); b84-87 const
  b0d5787a first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 116265..116612:
  348/348 exact.
- Quad b4 base 8b step2 64/64; b5 =
  0x8c+(o>=59) 64/64 (edge above ✓).
- T88 b4 = 0x0b step2 256/256; b5 =
  0x8d+(o>=123)+(o>=251) 256/256;
  edges o122->123 (n116479->116480
  ff/8d->01/8e) + o250->251
  (n116607->116608 ff/8e->01/8f).
- Consts ALL 4 EXACT: 80/70/66/69.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs (1 label nit, no geometry correction)
