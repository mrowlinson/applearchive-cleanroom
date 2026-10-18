# A-357 (viewer r8): Q-357 T10P293 @118701 — CONFIRM all legs

First-hand bed 118701..119048 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n118701 03291000 NEW, PB1 n118702
  3b635420 NEW.
- PBA88-PLAIN n118703-18 16x88B
  02000000 (M8 b28-31,80-83 16/16
  distinct ✓; VPOS 9 = b4+M8 over 88;
  b0 const 02, b5 const 9f; 16/16
  distinct; consts 79 ✓).
- C10-1SIG n118719-28 2b8b4e20 x10
  (M11 b24,26-31,80-83 b25-skipped
  const 3c ✓ 10/10; VPOS 12; b5
  const 9f; 10/10 diverge; consts
  72 ✓).
- QUAD88-4R n118729-792 02000000 x64
  88B-pay (VPOS 22 = b4,b5+M9+R11
  over 88; b5 0x9f+(o>=55), edge
  o54->55 n118783->118784 ff/9f->
  01/a0 ✓; NO frags; consts 66 ✓).
- T88-RING256 n118793-119048 sig
  25000000 (VPOS 18 = b4,b5+TM8+TR8
  partition over 0..87 ✓).
- Next P294 PB0 @119049 03291000
  (==P293PB0) + PB1 2b8b4e20
  (==P293C10sig) + PBA88 02000000 x16
  + C10 2b8b0e23 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M9 b19,25-27,35,80-83 by COL
  16/16 (16 distinct ✓).
- Quad R11 b28-34,84-87 rows 4/4 NO
  pairing EXACT first-hand (4 distinct
  row-tuples; r0 843cb8f3… distinct,
  r123 share prefix 17fc813f… but
  differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [40-43,76-79] by COL 16/16;
  R8 [29,30,34,35,80-83] by ROW 16/16
  UNPAIRED; SWAPPED tail orientation
  first-hand (M carries b76-79 col, R
  carries b80-83 row); b84-87 const
  d20ad28d first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 118701..119048:
  348/348 exact.
- Quad b4 base 93 step2 64/64; b5 =
  0x9f+(o>=55) 64/64 (edge above ✓).
- T88 b4 = 0x13 step2 256/256; b5 =
  0xa0+(o>=119)+(o>=247) 256/256;
  edges o118->119 (n118911->118912
  ff/a0->01/a1) + o246->247
  (n119039->119040 ff/a1->01/a2).
- Consts ALL 4 EXACT: 79/72/66/70.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
