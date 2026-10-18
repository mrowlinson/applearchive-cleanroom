# A-322 (viewer r7): Q-322 T10P258 P-head @106521 — CONFIRM all 3

First-hand bed 106521..106910 (qr7bed
extended; census RC=0 missing=0) +
P257T ref 106265..80 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 20370300 NEW, PB1 f8416e06 NEW,
  PBA 40811f74 x16 NEW (VPOS 9 exact
  b4+M8 b12-14,19,76-79; b5 const 40;
  NO pair in tier).
- C10-MS 6-sig map EXACT: 85c86106 x4
  @106539-42 + 2dbe3b03/8d963a03/
  5d533103/7d053403/851a3e03 x2
  @106543-48 (6 distinct ✓; VPOS 16
  exact b4+M15 b0-3,11,18-23,80-83;
  b5 const 40; 10/10 diverge).
- QUAD e0921f3a x64 NEW (VPOS 18 exact
  b4+QM6+R7+T4; b5 const 40).
- T88-RING 03000000 (==P255T sig), 88B
  payload all 256 ✓ (VPOS 17 exact
  b4,b5+TM9+TR6 partition over 0..87).
- Next P259 PB0 @106869 20370300
  (==P258PB0 REPEAT) + 106870 05016206
  NEW + PBA e0921f7a x16 @106871-86
  (P258Q-adjacent 3a->7a 1B-off last
  byte, derived) + C10 05016206
  @106887+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM6 b24,25,76-79 shared 16/16 x3
  vs row0 (clean).
- R7 b13,14,18-22 UNPAIRED 4/4 EXACT
  (d08f8179922dee/a5d2616e929df4/
  2ba0517412c0dc/9a8aa177927ed7 —
  first R with NO pairing ✓).
- Tails row-shared 4/4 distinct
  f2bc5daa/49f3db15/dab7ba8e/1469107b
  EXACT (no shared suffix: last bytes
  aa/15/8e/7b all differ).
- M-tails 16/16 ALL NEW vs P257T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM9 [18,19,27,34,
  35,80-83] by COL 16/16; TR6 [28,29,
  76-79] by ROW 16/16 UNPAIRED (16
  distinct); tails SPLIT b80-83 col /
  b76-79 row; b84-87 const 0b3bb263
  EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 106521..106868: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xeb+2off)&FF 256/256;
  b5=0x40+(off>=11)+(off>=139) 256/256;
  edges 106623->106624 ff/40->01/41 +
  106751->106752 ff/41->01/42.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 68 (b5-const), quad 66 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
