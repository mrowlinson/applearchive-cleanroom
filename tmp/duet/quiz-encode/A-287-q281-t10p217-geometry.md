# A-287 (viewer r3): Q-281 T10P217 P-head @92253 — CONFIRM all 3

First-hand bed 92253..92616 (q281.py new;
census 92269..92616 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 9e100000
  NEW, PB1 4ab22600 (==P216PB1), PBA
  4ab21602 (==P216PBA; VPOS 8 exact
  b4+M7 b48-50,76-79, b5 const d0).
- FRAG uneven 3-sig EXACT: 26x2 @92271,72
  4ab22600 (VPOS {b4,b80} pair-like, b5
  const) + 16x7 @92273,74,75,77,78,79,
  80 4ab21600 (VPOS 14 exact b4+M13
  b23,35,45-51,80-83, b5 const, 7/7) +
  1ex1 @92276 4ab21e00 singleton. NO
  pair/C8/B10.
- QUAD ae246b01 NEW (VPOS 19 exact
  b4,b5+M6+R11; b5-carry d0->d1 @92287->
  92288 ff->01 edge).
- T-RING fe4ab216 NEW (VPOS 14 exact =
  b4,b5+M6+R6 partition).
- Next @92601 56110000 NEW + 92602
  8aac2200 NEW + 92603/04 a1c82a02 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,76-79 shared 16/16 x3 vs
  row0.
- R7 b35,46,47,48-51 r0==r2==r3
  TRIPLE-PAIRED 2/4 EXACT (58958bd1ffff9c
  x3; r1 18aca8917e0f73) — fixed analyzer
  states pairing exactly right.
- Tails row-shared 4/4 distinct
  5ee9875d/97eccbbd/bde9875d/ece9875d
  EXACT; r0/r2/r3 share last 3B e9875d ✓.
- M-tails 16/16 ALL NEW vs P216T (row-0
  reference, true novelty).
- T-ring STANDARD: M6 b13,14,76-79 by COL
  16/16; R6 b6,7,72-75 by ROW 16/16
  UNPAIRED (16 distinct); tails const (1
  ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 92253..92600: 348/348
  exact (whole tier).
- T-ring b4=(0x73+2off)&FF 256/256;
  b5=0xd1+(off>=71)+(off>=199) 256/256;
  edges 92415->92416 ff/d1->01/d2 +
  92543->92544 ff/d2->01/d3.
- Consts ALL 4 EXACT: PBA 76 (b5-const
  ✓), F16 70 (b5-const ✓), quad 65
  (b5 varies carry ✓), T 70.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
