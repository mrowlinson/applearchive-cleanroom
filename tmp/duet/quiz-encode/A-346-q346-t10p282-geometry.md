# A-346 (viewer r8): Q-346 T10P282 @114873 — CONFIRM all legs

First-hand bed 114873..115220 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT (C10 + QUAD all 84B
  first-hand).
- PB0 n114873 9ef00700 NEW, PB1 n114874
  cb3de10f NEW.
- PBA16-PLAIN n114875-90 e0857ffe x16
  (M8 b12,13,14,19,76-79 16/16
  distinct ✓; VPOS 9 = b4+M8; b0
  const e0, b5 const 81; 16/16
  distinct; consts 75 ✓).
- C10-4SIG ordered map first-hand:
  3582e40f x6 @114891-96 + 4dffe70f
  @114897 + 8d59ea0f @114898 +
  ad85e10f x2 @114899-900 (counts 6+1
  +1+2 ✓; M13 b0-2,11,18-22,80-83
  10/10 ✓; VPOS 14; b5 const 81;
  10/10 diverge; consts 70 ✓).
- QUAD2s-3P n114901-964 c09b7fe2 x64
  1-sig 84B (VPOS 20 =
  b4,b5+QM7+R7+T4; b20-skipped const
  93 ✓; NO frags; consts 64 ✓).
- T88-RING256 n114965-115220 sig
  0f000000 (VPOS 18 = b4,b5+TM9+TR7
  partition over 0..87 ✓).
- Next P283 PB0 @115221 9ef00700
  (==P282PB0) + PB1 4513e30f NEW + PBA
  c09b7fe2 x16 + C10-2SIG 4513e30f x6
  + 4513f307 x4 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M7 b24,25,26,76-79 shared 16/16
  x3 vs row0 (row0 16 distinct ✓).
- Quad R7 b12-14,18,19,21,22 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT first-hand
  (r123 72fabf3a6f842e x3; r0
  b280ae92788e26 distinct).
- Tails b80-83 row-shared 4/4 distinct
  first-hand: dd6e42df/e1a9fa40/
  06aafa40/227a1141.
- T88 M9 [18,19,27,34,35,80-83] by COL
  16/16; R7 [28,29,30,76-79] by ROW
  16/16 UNPAIRED; tails SPLIT b80-83
  col / b76-79 row; b84-87 const
  63fa9206 first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 114873..115220:
  348/348 exact.
- Quad b4 base ab step2 64/64; b5 =
  0x81+(o>=43) 64/64; edge o42->43
  (n114943->114944 ff/81->01/82,
  mid-row2 ✓).
- T88 b4 = 0x2b step2 256/256; b5 =
  0x82+(o>=107)+(o>=235) 256/256;
  edges o106->107 (ff/82->01/83) +
  o234->235 (ff/83->01/84).
- Consts ALL 4 EXACT: 75/70/64/70.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
