# A-302 (viewer r3): Q-296 T10P232 P-head @97473 — CONFIRM all 3

First-hand bed 97473..97840 (q296.py new,
88B-aware; census 97489..97840 RC=0
missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 053b0100 NEW, PB1 dd1a3f01 NEW,
  PBA-SPLIT8 dd1adf14 x8 @97475..82 +
  dd1a2f16 x8 @97483..90 NEW (VPOS 11
  exact b4+M8+split2 b21-23,31,76-79 +
  b2/b3 df14/2f16 exact; b22 half0
  {223,254}→half1 {223} + b23 half0
  {117,119}→half1 {233} — const-in-half1
  ✓✓; b5 const f9).
- PAIR 97491..97492 dd1a7f02 NEW (VPOS
  {b4,b80} ONLY exact).
- PBC8 dd1a3f01 (==PB1) NEW (VPOS 13
  exact b4+M12 b22,23,30-35,80-83, b5
  const f9).
- QUAD dd1abf13 NEW (VPOS 22 exact
  b4,b5+M8+R8+T4; b5-carry f9->fa @97535->
  97536 ff->01 edge).
- T88-RING 01000000 (==P231T sig ✓), 88B
  payload all 256 ✓ (VPOS 19 exact =
  b4,b5+M9+R8 partition over 0..87).
- Next @97821 043b0100 NEW + 97822
  dd1a3f01 (==P232PB1) + 97823..36
  dd1abf13 x14 (==P232Q sig ✓).

## 2. quad + T-ring: CONFIRM
- Quad M8 b36-39,76-79 shared 16/16 x3 vs
  row0.
- R8 b22,23,30-35 r1==r2 PAIRED 3/4 EXACT
  (21578e7f54512a07 x2; r0/r3 distinct).
- Tails row-shared 4/4 distinct
  aeef66e5/acab63db/d6ab63db/d3703d27
  EXACT; r1/r2 share last 3B ab63db ✓
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P231T (row-0
  reference, true novelty).
- T88-ring STANDARD: M9 [18,27,39,46,47,
  80-83] by COL 16/16; R8 [40-43,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col (16) / b76-79
  row (16); b84-87 const (1 ring-wide ✓).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 97473..97820: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x3b+2off)&FF 256/256;
  b5=0xfa+(off>=99)+(off>=227) 256/256;
  edges 97663->97664 ff/fa->01/fb +
  97791->97792 ff/fb->01/fc.
- Consts ALL 4 EXACT (workaround counts
  verified): PBA 73 (b5-const ✓), PBC 71
  (b5-const ✓), quad 62 (b5 varies
  carry ✓), T88 69 (88-19 ✓).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
