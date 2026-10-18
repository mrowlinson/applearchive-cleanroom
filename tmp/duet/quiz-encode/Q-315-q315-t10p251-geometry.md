# Q-315 (writer2 s20): T10P251 P-head @104085 — geometry?

Own first-hand bed 104085..104432 (census RC=0
missing=0), staged p251-patch.txt, sweep
348/348 err 0 (try-p251; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 90fc0200 (==P250PB0), PB1
  5d16fd05 NEW, PBA 00882f46 x16
  (P250Q-adjacent 26->46; VPOS 8:
  b4+M7 b36-38,76-79; b5 const 2d;
  NO pair in tier).
- B10 single-sig 5d16fd05 x10 (==PB1
  sig; VPOS 12: b4+M11 b36-42,80-83;
  b42 IN M-range; b5 const 2d; 10/10
  diverge).
- QUAD 00882f46 x64 (==PBA sig; VPOS
  19: b4+QM7+b42+R6+T4; b5 const 2d).
- T88-RING 05000000 (==P249T sig), 88B
  payload (VPOS 17 =
  b4,b5+TM7+TR8 partition over 0..87).
- Next P252 PB0 @104433+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b34,35,43,76-79 shared
  16/16 x3 vs row0.
- b42: row-XOR X=[00,06,06,06] 64/64
  AND ADD A=[0,fa,fa,fa] 64/64 — TIE
  first-hand (M42 col-vector 4-valued
  {d6,96,56,16}, low-nibble const 6;
  staged XOR by b42-family precedent,
  flagged as tie).
- R6 b36-41 r1==r2==r3 TRIPLE 2/4
  EXACT (865bd276b11b x3; r0
  dc5dc1973145 distinct).
- Tails row-shared 4/4 distinct
  50155041/7e8da7ed/a88da7ed/d28da7ed;
  r1/r2/r3 share last 3B 8da7ed
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P250T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [52-54,80-83]
  by COL 16/16; TR8 [38,39,46,47,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const d311a27a (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 104085..104432: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xe3+2off)&FF 256/256;
  b5=0x2d+(off>=15)+(off>=143) 256/256;
  edges 104191->104192 ff/2d->01/2e +
  104319->104320 ff/2e->01/2f?
- Consts ALL 4: PBA 76 (b5-const), B10
  72 (b5-const), quad 65 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
