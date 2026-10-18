# A-356 (viewer r8): Q-356 T10P292 @118353 — CONFIRM all legs

First-hand bed 118353..118700 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n118353 436f1300 NEW, PB1 n118354
  2b81e720 NEW.
- PBA88-PLAIN n118355-70 16x88B
  02000000 (M6 b6,7,80-83 16/16
  distinct ✓; VPOS 7 = b4+M6 over 88;
  b0 const 02, b5 const 9c; 16/16
  distinct; consts 81 ✓).
- C10-2SIG ordered map first-hand:
  08075220 x7 @118371-77 + 84032910 x3
  @118378-80 (2-sig 7+3 ✓; M17
  b0-3,6-8,10,11,48-51,80-83
  b9-skipped const 00 ✓ 10/10; VPOS
  18; b5 const 9c; 10/10 diverge;
  consts 66 ✓).
- QUAD88-4R n118381-444 01000000 x64
  88B-pay (VPOS 19 = b4,b5+M7+R10
  over 88; b5 0x9c+(o>=19), edge
  o18->19 n118399->118400 ff/9c->
  01/9d ✓; NO frags; consts 69 ✓).
- T88-RING256 n118445-700 sig 11000000
  (VPOS 17 = b4,b5+TM8+TR7 partition
  over 0..87 ✓).
- Next P293 PB0 @118701 03291000 NEW +
  PB1 3b635420 NEW + PBA88 02000000
  x16 + C10 2b8b4e20 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M7 b13,14,15,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R10 b6,7,52-55,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples; r0 c36f025c…
  distinct, r123 share prefix 8b87eb58…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [8,9,10,19,80-83] by COL
  16/16; R7 [13,14,15,76-79] by ROW
  16/16 UNPAIRED; tails SPLIT b80-83
  col / b76-79 row (standard); b84-87
  const bea6f6d3 first-hand
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 118353..118700:
  348/348 exact.
- Quad b4 base db step2 64/64; b5 =
  0x9c+(o>=19) 64/64 (edge above ✓).
- T88 b4 = 0x5b step2 256/256; b5 =
  0x9d+(o>=83)+(o>=211) 256/256;
  edges o82->83 (n118527->118528
  ff/9d->01/9e) + o210->211
  (n118655->118656 ff/9e->01/9f).
- Consts ALL 4 EXACT: 81/66/69/71.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
