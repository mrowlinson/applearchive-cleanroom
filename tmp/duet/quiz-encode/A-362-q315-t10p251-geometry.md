# A-362 (viewer r10): Q-315 T10P251 P-head @104085 — CONFIRM all 3

First-hand bed 104085..104432 (q315
own; census RC=0 missing=0, 348/348)
+ P250 refs 103829..44 (T row0) +
103765 (Q) + P249T 103481/36 re-read
+ P252 window 104433..56.

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 90fc0200 (==P250PB0 re-read
  @103737 ✓), PB1 5d16fd05 NEW, PBA
  00882f46 x16 @104087..102 (P250Q
  00882f26 re-read @103765, 26->46
  1B-off last byte ✓; VPOS 8 exact
  b4+M7 b36-38,76-79; b5 const 2d;
  16/16 distinct, NO pair).
- B10 single-sig 5d16fd05 x10 @104103..12
  (==PB1 ✓; VPOS 12 exact b4+M11
  b36-42,80-83; b42 IN range; b5
  const 2d; 10/10 diverge).
- QUAD 00882f46 x64 @104113..76 (==PBA
  ✓; VPOS 19 exact b4+QM7+b42+R6+T4;
  b5 const 2d).
- T88-RING 05000000 x256 (==P249T sig
  re-read @103481/36 ✓), 88B payload
  all 256 ✓ (VPOS 17 exact
  b4,b5+TM7+TR8 over 0..87).
- Next P252 PB0 @104433 80fc0200 NEW +
  104434 5d169d05 NEW + PBA dc65d159
  x16 @104435..50 + C10 8cc03106
  @104451+ multi-sig (104455 46e01803;
  window resolved).

## 2. quad + T-ring: CONFIRM (tie stands)
- Quad QM7 b34,35,43,76-79 shared
  16/16 x3 vs row0.
- b42: row-XOR X=[00,06,06,06] 64/64
  AND ADD A=[0,fa,fa,fa] 64/64 — TIE
  first-hand (M42 row-0 col-vector
  4-valued {d6,96,56,16} exact,
  low-nibble const 6; staged XOR
  consistent with tie).
- R6 b36-41 r1==r2==r3 TRIPLE 16/16
  cols, 2/4 EXACT (865bd276b11b x3;
  r0 dc5dc1973145 distinct; col0
  hexes exact).
- Tails row-shared 4/4 distinct
  50155041/7e8da7ed/a88da7ed/d28da7ed
  EXACT; r1/r2/r3 share last 3B
  8da7ed ✓.
- M-tails 16/16 ALL NEW vs P250T row-0
  (quad b76-79 16 distinct col-vals,
  zero overlap with P250T-row0
  1d282bad; true novelty; T-TM7 and
  T-b7679 readings also 16/16 new).
- T88-ring STANDARD: TM7 [52-54,80-83]
  by COL 16/16; TR8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const d311a27a EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 104085..104432: 348/348
  exact (pay[4:6]==LE16((n<<1)|1),
  whole tier incl 88B cells).
- T88-ring b4=(0xe3+2off)&FF 256/256;
  b5=0x2d+(off>=15)+(off>=143) 256/256;
  edges 104191->104192 ff/2d->01/2e +
  104319->104320 ff/2e->01/2f exact.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  B10 72 (b5-const), quad 65 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers (observed==staged per
  group). NO D-class dips (group
  sig/size norms uniform, lencode
  clean).

## geometry agrees on all 3 legs
