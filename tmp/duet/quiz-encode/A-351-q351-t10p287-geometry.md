# A-351 (viewer r8): Q-351 T10P287 @116613 — CONFIRM all legs

First-hand bed 116613..116960 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n116613 85620b00 NEW, PB1 n116614
  4c0ac516 NEW.
- PBA88-PLAIN n116615-30 16x88B
  01000000 (M10 b8,13-17,80-83 16/16
  distinct ✓; VPOS 11 = b4+M10 over
  88; b0 const 01, b5 const 8f; 16/16
  distinct; consts 77 ✓).
- C10-1SIG n116631-40 86148a2d x10
  (M11 b13-19,80-83 10/10 ✓; VPOS 12;
  b5 const 8f; 10/10 diverge; consts
  72 ✓).
- QUAD88-4R n116641-704 02000000 x64
  88B-pay (VPOS 21 = b4+M9+R11 over
  88; b5 const 8f = full odd lencode
  ✓; NO frags; consts 67 ✓).
- T88-RING256 n116705-960 sig 2d000000
  (VPOS 18 = b4,b5+TM8+TR8 partition
  over 0..87 ✓).
- Next P288 PB0 @116961 0ac51600 NEW +
  PB1 3bf3942d NEW + PBA88 02000000
  x16 + C10 3bf3942d (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M9 b16-19,23,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R11 b8-11,20,21,22,84-87 rows
  4/4 NO pairing EXACT first-hand (4
  distinct row-tuples; r0 19318ff0…
  distinct, r123 share 11B-prefix
  d9171fcdeadc but differ in tail
  bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M8 [28-31,80-83] by COL 16/16;
  R8 [20-23,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row (standard); b84-87 const
  1a509e70 first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 116613..116960:
  348/348 exact.
- T88 b4 = 0xc3 step2 256/256; b5 =
  0x8f+(o>=31)+(o>=159) 256/256;
  edges o30->31 (n116735->116736
  ff/8f->01/90) + o158->159
  (n116863->116864 ff/90->01/91).
- Consts ALL 4 EXACT: 77/72/67/70.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
