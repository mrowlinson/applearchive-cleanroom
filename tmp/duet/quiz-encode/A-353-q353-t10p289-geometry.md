# A-353 (viewer r8): Q-353 T10P289 @117309 — CONFIRM all legs

First-hand bed 117309..117656 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n117309 0fc51600 NEW, PB1 n117310
  3bf3f420 NEW.
- PBA88-PLAIN n117311-26 16x88B
  02000000 (M7 b52,53,54,80-83 16/16
  distinct ✓; VPOS 8 = b4+M7 over 88;
  b0 const 02, b5 const 94; 16/16
  distinct; consts 80 ✓).
- C10-2SIG ordered map first-hand:
  3bf3f420 x7 @117327-33 + 3bf3f41a x3
  @117334-36 (2-sig 7+3 ✓; M12
  b3,35,46-51,80-83 10/10 ✓; VPOS 13;
  b5 const 94; 10/10 diverge; consts
  71 ✓).
- QUAD88-4R n117337-400 01000000 x64
  88B-pay (VPOS 18 = b4,b5+M6+R10
  over 88; b52-skipped const d1 ✓;
  b5 0x94+(o>=39), edge o38->39
  n117375->117376 ff/94->01/95 ✓; NO
  frags; consts 70 ✓).
- T88-2SIG256 n117401-656 sig 1f/1d
  col-split c<9 (144+112 = 9+7 per row
  x16 rows ✓; VPOS 17 =
  b4,b5+TM9+TR6 partition over 0..87,
  b0 inside TM9 ✓).
- Next P290 PB0 @117657 5f6f1300 NEW +
  PB1 ccbede26 NEW + PBA88 02000000
  x16 + C10-3SIG 1b19db26 x7 +
  bb9cdb26 + 8bf4d626 x2 (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,80-83 by COL 16/16 (16
  distinct ✓).
- Quad R10 b11,50,51,53,54,55,84-87
  rows 4/4 NO pairing EXACT first-hand
  (4 distinct row-tuples; r0 bbb12ce5…
  distinct, r123 share prefix c7d82676…
  but differ in tail bytes).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 col-split b0 = 1f iff col<9 else
  1d, 256/256 EXACT; M9
  [b0,9,10,11,20,80-83] by COL 16/16;
  R6 [6,7,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row; b84-87 const 8536000f
  first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 117309..117656:
  348/348 exact.
- Quad b4 base b3 step2 64/64; b5 =
  0x94+(o>=39) 64/64 (edge above ✓).
- T88 b4 = 0x33 step2 256/256; b5 =
  0x95+(o>=103)+(o>=231) 256/256;
  edges o102->103 (n117503->117504
  ff/95->01/96) + o230->231
  (n117631->117632 ff/96->01/97).
- Consts ALL 4 EXACT: 80/71/70/71.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
