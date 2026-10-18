# A-299 (viewer r3): Q-293 T10P229 P-head @96429 — CONFIRM + 3 fixes

First-hand bed 96429..96776 (q293.py new;
census 96097..97124 RC=0 missing=0).

## 1. shape: CONFIRM + pair-byte fix
- 348 cells sizes {(100,84)}. PB0 994e0000
  NEW, PB1 e6969900 NEW, PBA e696d109 NEW
  (VPOS 7 exact b4+M6 b24,25,76-79, b5
  const f1).
- PAIR-3T 96447..96448 32f79900 NEW (VPOS
  {b4,b80,81,82} exact — diff b4+b80-82
  ✓). CORRECTION: b83 same 0x60 (96
  decimal) — Q-prose "96" reads 0x96
  under the hex convention (≠ 0x60
  observed); agree if decimal-intended.
- PBC8 32f74900 NEW (VPOS 14 exact b4+M13
  b20,21,25-31,80-83, b5 const f1).
- QUAD 32f7c107 NEW (VPOS 21 exact
  b4,b5+M7+R7+b31+T4; b5-carry f1->f2
  @96511->96512 ff->01 edge).
- T-RING e096d758 NEW (VPOS 18 exact =
  b4,b5+M8+R8 partition).
- Next @96777 984e0000 NEW + 96778
  32f79900 (==P229PAIR) + 96779/80
  32f7f108 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M7 b21-23,76-79 shared 16/16 x3 vs
  row0.
- b31 row-add A=[0,1,0,0] 64/64 vs row-0
  M31 (r1-only +1; rows 0,2,3 identical
  ✓; 32 distinct ✓).
- R7 b24-30 r0==r2 EVEN-PAIRED 3/4 EXACT
  (fabc851eb404f9 x2; r1/r3 distinct).
- Tails row-shared 4/4 distinct
  d08feaa6/29215901/2690eaa6/26d52267
  EXACT; r0/r2 share last 3B 90eaa6 ✓
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P228T row-0
  (ref set size 1 — DUAL-ring row-0
  collapses to R7-row-0 value; novelty
  16 either way).
- T-ring STANDARD: M8 [32,33,38,39,72-75]
  by COL 16/16; R8 [21-23,31,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT (b72-75 16 col + b76-79 16
  row, NOT const ✓); b80-83 const (1 ✓).

## 3. counters + dips: CONFIRM + 2 const fixes
- Odd-lencode ALL 96429..96776: 348/348
  exact (whole tier).
- T-ring b4=(0x13+2off)&FF 256/256;
  b5=0xf2+(off>=119)+(off>=247) 256/256;
  edges 96639->96640 ff/f2->01/f3 +
  96767->96768 ff/f3->01/f4.
- CORRECTIONS: PBA consts 77 (not 76;
  VPOS 7 → 84-7); PBC consts 70 (not 69;
  VPOS 14 → 84-14). (4th head-group
  off-by-one: filed = 84-VPOS-1 in Q-292
  PBA/PBC + Q-293 PBA/PBC — analyzer
  consts bug on head groups?) Quad 63 ✓
  (varies). T 66 ✓.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; b83 0x60 + PBA 77 + PBC 70
