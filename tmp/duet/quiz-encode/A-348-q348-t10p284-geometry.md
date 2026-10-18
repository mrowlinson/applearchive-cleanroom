# A-348 (viewer r8): Q-348 T10P284 @115569 — CONFIRM all legs

First-hand bed 115569..115916 (qr8bed own
oracle runs; census RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x28, (104,88)
  x320} EXACT (PBA + C10 84B, QUAD88 +
  T88 88B first-hand).
- PB0 n115569 99f00700 NEW, PB1 n115570
  4513630f NEW.
- PBA16-STEP n115571-86 5d3431f6 x16
  (M9 b6-10,76-79 16/16 distinct ✓;
  VPOS 11 = b4,b5+M9; b0 const 5d;
  b5 0x86+(o>=13), edge o12->13
  n115583->115584 ff/86->01/87 ✓;
  16/16 distinct; consts 73 ✓).
- C10-1SIG n115587-96 c432f015 x10
  (M11 b6-8,48-51,80-83 10/10 ✓; VPOS
  12; b5 const 87; 10/10 diverge;
  consts 72 ✓).
- QUAD88-4R n115597-660 01000000 x64
  88B-pay (VPOS 18 = b4+M7+R10 over
  88; b5 const 87; NO frags; consts
  70 ✓).
- T88-RING256 n115661-916 sig 14000000
  (VPOS 17 = b4,b5+TM8+TR7 partition
  over 0..87 ✓).
- Next P285 PB0 @115917 19f80a00 NEW +
  PB1 ddbef415 NEW + PBA88 01000000
  x16 + C10 cd23fd15 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad M7 b13,14,15,80-83 by COL 16/16
  (16 distinct ✓).
- Quad R10 b6,7,52-55,84-87 rows 4/4
  NO pairing EXACT first-hand (4
  distinct row-tuples: 1b36beda5c67…
  /534c7bdbb26de4e…/534c7bdbb26de78…
  /534c7bdbb26d0c8…).
- b80-83 col-shared ✓ / b84-87
  row-shared ✓ (4 distinct rows).
- T88 M8 [8,9,10,19,80-83] by COL
  16/16; R7 [13,14,15,76-79] by ROW
  16/16 UNPAIRED; tails SPLIT b80-83
  col / b76-79 row; b84-87 const
  309f7eaa first-hand (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 115569..115916:
  348/348 exact.
- T88 b4 = 0x9b step2 256/256; b5 =
  0x87+(o>=51)+(o>=179) 256/256;
  edges o50->51 (n115711->115712
  ff/87->01/88) + o178->179
  (n115839->115840 ff/88->01/89).
- Consts ALL 4 EXACT: 73/72/70/71.
- varpos partitioned exact, 0
  stragglers. NO D-class dips.

## geometry agrees on all legs
