# A-349 (viewer r8): Q-349 T10P285 @115917 — CONFIRM all legs

First-hand bed 115917..116264 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x12, (104,88)
  x336} EXACT (PB0/PB1/C10 84B;
  PBA88 + QUAD88 + T88 88B first-hand).
- PB0 n115917 19f80a00 NEW, PB1 n115918
  ddbef415 NEW.
- PBA88-PLAIN n115919-34 16x88B
  01000000 (M9 b28-32,80-83 16/16
  distinct ✓; VPOS 10 = b4+M9 over
  88; b0 const 01, b5 const 89; 16/16
  distinct; consts 78 ✓).
- C10-1SIG n115935-44 cd23fd15 x10
  (M12 b24-31,80-83 10/10 ✓; VPOS 13;
  b5 const 89; 10/10 diverge; consts
  71 ✓).
- QUAD88-4R n115945-116008 01000000
  x64 88B-pay (VPOS 21 =
  b4,b5+M8+R11 over 88; b5
  0x89+(o>=23), edge o22->23 n115967->
  115968 ff/89->01/8a ✓; NO frags;
  consts 67 ✓).
- T88-RING256 n116009-264 sig 16000000
  (VPOS 16 = b4,b5+TM7+TR7 partition
  over 0..87 ✓).
- Next P286 PB0 @116265 1df80a00 NEW +
  PB1 cd23fd15 (==P285C10sig) + PBA88
  01000000 x16 + C10 cd236d10 (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad M8 b25,26,27,35,80-83 by COL
  16/16 (16 distinct ✓).
- Quad R11 b28-34,84-87 rows 4/4 NO
  pairing EXACT first-hand (4 distinct
  row-tuples: 413c512d95c6…/fdbce3ce…
  f2a2…/fdbce3ce…f217…/fdbce3ce…f2ea…).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓.
- T88 M7 [40,41,42,76-79] by COL 16/16;
  R7 [29,34,35,80-83] by ROW 16/16
  UNPAIRED; SWAPPED tail orientation
  first-hand (M carries b76-79 col, R
  carries b80-83 row — NOT the
  standard split); b84-87 const
  e4654e71 first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 115917..116264:
  348/348 exact.
- Quad b4 base d3 step2 64/64; b5 =
  0x89+(o>=23) 64/64 (edge above ✓).
- T88 b4 = 0x53 step2 256/256; b5 =
  0x8a+(o>=87)+(o>=215) 256/256;
  edges o86->87 (n116095->116096
  ff/8a->01/8b) + o214->215
  (n116223->116224 ff/8b->01/8c).
- Consts ALL 4 EXACT: 78/71/67/72.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
