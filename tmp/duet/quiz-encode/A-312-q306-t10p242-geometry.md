# A-312 (viewer r3): Q-306 T10P242 P-head @100953 — CONFIRM + 1 CORRECTION

First-hand bed 100953..101316 (q306.py
new, 88B-aware; census extended
100969..101316 RC=0 missing=0 per-N).

## 1. shape: CONFIRM + CORRECTION
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 4b620100 NEW, PB1 6197c402 NEW,
  PBA 608fd732 NEW (VPOS 10 exact
  b4+M9 b12-15,19,76-79, b5 const 14;
  NO pair in tier).
- C10-MS 6-sig map EXACT: bd7dc602 x3
  @100971-73 + f5c1ce02/6517cb02/
  1dfac902/f5c1ce02/c5f9cd02/9d6fcf02/
  1dfac902 @100974-80 (6 distinct ✓;
  VPOS 14 exact b4+M13 b0-2,11,18-22,
  80-83; b5 const 14; 10/10 diverge).
- QUAD 0080773c NEW (VPOS 21 exact
  b4,b5+M8+R7+T4 — b20 skipped as
  staged; b5-carry 14->15 @100991->
  100992 ff->01 edge).
- T88-RING sig 02000000 value ✓, 88B
  payload all 256 ✓ (VPOS 19 exact
  b4,b5+M9+R8 partition over 0..87).
- CORRECTION: parenthetical
  "(==P234/235/241T sig)" is wrong on
  241T: P241T @100697 re-read first-hand
  = 03000000 (A-311 CONFIRM, NEW). P242T
  02000000 ==P234/235T only.
- Next @101301 4b620100 (==P242PB0
  REPEAT ✓) + 101302 3d31c602 NEW +
  101303..16 0080773c (==P242Q sig, x14
  ✓).

## 2. quad + T-ring: CONFIRM
- Quad M8 b24-27,76-79 shared 16/16 x3
  vs row0.
- R7 b12-14,18,19,21,22 r2==r3 PAIRED
  3/4 EXACT (b20f76d47c32b9 x2; r0
  32ce7f3478c7b0 distinct; r1
  b20f76d07c32b9 1B-off d4-vs-d0 ✓).
- Tails row-shared 4/4 distinct
  049680e9/2930e3e7/45bd1e06/6fbd1e06
  EXACT; r2/r3 share last 3B bd1e06
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P241T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [18,19,27,34,35,
  80-83] by COL 16/16; R8 [28-31,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT verified explicitly
  (b80-83 col-shared 16 cols, b76-79
  row-shared 16 rows); b84-87 const
  2771a8dd EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 100953..101300: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x6b+2off)&FF 256/256;
  b5=0x15+(off>=75)+(off>=203) 256/256;
  edges 101119->101120 ff/15->01/16 +
  101247->101248 ff/16->01/17.
- Consts ALL 4 EXACT: PBA 74 (b5-const),
  C10 70 (b5-const), quad 63 (b5 varies
  carry), T88 69 (88-19).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs (1 sig-ref correction)
