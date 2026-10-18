# Q-344 (writer2 s20): T10P280 P-head @114177 — geometry?

Own first-hand bed 114177..114524 (census RC=0
missing=0), staged p280-patch.txt, sweep
348/348 err 0 (try-p280; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 58ae0700 NEW, PB1 2557520f
  NEW, PBA16-PLAIN c09417fb x16
  @114179-94 (VPOS 10: b4+M9
  b15,21-23,31,76-79; b0 const c0, b5
  const 7c; NO pair in tier).
- C10-1SIG single-sig EXACT map: 2557520f
  x10 @114195-204 (VPOS 13: b4+M12
  b22,23,30-35,80-83; b5 const 7c;
  10/10 diverge; head-sig == PB1 sig).
- QUAD1s 1-sig c09417fb x64 (VPOS 19:
  b4+QM7+R7+T4; b5 const 7c).
- T88-RING 0e000000, 88B payload (VPOS
  18 = b4,b5+TM9+TR7 partition over
  0..87).
- Next P281 PB0 @114525+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0; NO frags (all positions
  COL-pure or ROW-pure, 0 MIXED).
- R7 b22,23,30-34 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  43bcbf7ed5979d x3; r0 ffca8b7ff5c277
  distinct).
- Tails row-shared 4/4 distinct
  75713981/38ac6799/b7ac6799/163bd7bf;
  r1/r2 share last 3B ac6799.
- M-tails 16/16 ALL NEW vs P279T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM9
  [30,31,39,46,47,80-83] by COL 16/16;
  TR7 [40-42,76-79] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b80-83 col / b76-79 row; b84-87
  const 0636193d (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 114177..114524: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xbb+2off)&FF 256/256;
  b5=0x7c+(off>=35)+(off>=163) 256/256;
  edges 114303->114304 ff/7c->01/7d +
  114431->114432 ff/7d->01/7e?
- Consts ALL 4: PBA 74 (b5-const), C10
  71 (b5-const), quad 65 (b5-const),
  T88 70 (88-18)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
