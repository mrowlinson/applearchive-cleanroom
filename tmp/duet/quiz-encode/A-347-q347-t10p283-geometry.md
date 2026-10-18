# A-347 (viewer r8): Q-347 T10P283 @115221 — CONFIRM all legs

First-hand bed 115221..115568 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT (C10 + QUAD all 84B
  first-hand).
- PB0 n115221 9ef00700 SAME-as-P282PB0
  ✓ (byte-equal first-hand), PB1
  n115222 4513e30f NEW.
- PBA16-PLAIN n115223-38 c09b7fe2 x16
  (M7 b36,37,38,76-79 16/16 distinct
  ✓; VPOS 8 = b4+M7; b0 const c0,
  b5 const 84; 16/16 distinct; consts
  76 ✓).
- C10-2SIG ordered map first-hand:
  4513e30f x6 @115239-44 + 4513f307 x4
  @115245-48 (2-sig 6+4 ✓; M16
  b2,3,34-43,80-83 10/10 ✓; VPOS 17;
  b5 const 84; 10/10 diverge; consts
  67 ✓).
- QUAD2s-3P n115249-312 c09b7f62 x64
  1-sig 84B (VPOS 18 =
  b4+M6+b42+R6+T4; b5 const 84;
  consts 66 ✓).
- T88-RING256 n115313-568 sig 07000000
  (VPOS 15 = b4,b5+TM6+TR7 partition
  over 0..87 ✓).
- Next P284 PB0 @115569 99f00700 NEW +
  PB1 4513630f NEW + PBA 5d3431f6 x16
  + C10 c432f015 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M6 b34,43,76-79 shared 16/16 x3
  vs row0 (row0 16 distinct ✓).
- Quad R6 b36-41 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT first-hand
  (r123 9d592674f113 x3; r0
  285f5f3c51e4 distinct).
- Tails b80-83 row-shared 4/4 distinct
  first-hand: 1ebc3c63/9a7d1825/
  bf7d1825/e47d1825.
- b42 NIBSPLIT EXACT first-hand: hi
  nibble == coltab 733f373777bff773
  64/64; lo nibble == rowtab (r0->5,
  r123->9) 64/64.
- T88 M6 [52,53,80-83] by COL 16/16;
  R7 [38,46,47,76-79] by ROW 16/16
  UNPAIRED; tails SPLIT b80-83 col /
  b76-79 row; b84-87 const a8fd2c45
  first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 115221..115568:
  348/348 exact (quad b5-const 84 =
  full odd lencode ✓).
- T88 b4 = 0xe3 step2 256/256; b5 =
  0x84+(o>=15)+(o>=143) 256/256;
  edges o14->15 (n115327->115328
  ff/84->01/85) + o142->143
  (n115455->115456 ff/85->01/86).
- Consts ALL 4 EXACT: 76/67/66/73.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
