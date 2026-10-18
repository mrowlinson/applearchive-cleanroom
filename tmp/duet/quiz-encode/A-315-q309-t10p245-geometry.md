# A-315 (viewer r3): Q-309 T10P245 P-head @101997 — CONFIRM all 3

First-hand bed 101997..102360 (q309.py
new, 88B-aware; census extended
102013..102360 RC=0 missing=0 per-N).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 d46f0100 NEW, PB1 b553d702 NEW,
  PBA 2085c72e NEW (VPOS 7 exact b4+M6
  b24,25,76-79, b5 const 1c; NO pair in
  tier).
- C10-2SIG map EXACT: 7d38be05 x3
  @102015-17 + 7d38de02 x7 @102018-24
  (VPOS 19 exact b4,b5+M17 b2,3,21-31,
  80-83; b5-CARRY 1c->1d @102015->102016
  ff->01 edge INSIDE block ✓; 10/10
  diverge).
- QUAD 2085c72e x64 (==PBA sig ✓; VPOS
  20 exact b4+QM8+R7+T4; b5 const 1d).
- T88-RING 02000000 (==P244T sig ✓
  direct cross-check; P242/243T same
  value per A-314), 88B payload all 256
  ✓ (VPOS 17 exact b4,b5+TM7+TR8
  partition over 0..87).
- Next P246 PB0 @102345 acdf0200 NEW +
  102346 7d38be05 (==P245C10 sig) +
  102347..60 2085c74e x14 NEW (window
  resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b21-23,31,76-79 shared 16/16
  x3 vs row0 (clean, no b42: b42 const
  0x95 all 64 ✓).
- R7 b24-30 r1==r2==r3 TRIPLE 2/4
  EXACT (ba7c80a31478a7 x3; r0
  933cc422d4f27c distinct).
- Tails row-shared 4/4 distinct
  c26f98d7/78214c1b/a2214c1b/cc214c1b
  EXACT; r1/r2/r3 share last 3B 214c1b
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P244T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [40-42,76-79]
  by COL 16/16 (b42 in T-M ✓); TR8
  [25-27,35,80-83] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  verified explicitly (b76-79 col-shared
  16 cols, b80-83 row-shared 16 rows);
  b84-87 const b196ffe1 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 101997..102344: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x93+2off)&FF 256/256;
  b5=0x1d+(off>=55)+(off>=183) 256/256;
  edges 102143->102144 ff/1d->01/1e +
  102271->102272 ff/1e->01/1f.
- Consts ALL 4 EXACT: PBA 77 (b5-const),
  C10 65 (b5-carry), quad 64 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
