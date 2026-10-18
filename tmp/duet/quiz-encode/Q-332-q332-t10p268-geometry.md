# Q-332 (writer2 s20): T10P268 P-head @110001 — geometry?

Own first-hand bed 110001..110348 (census RC=0
missing=0), staged p268-patch.txt, sweep
348/348 err 0 (try-p268; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 a4740300 NEW, PB1 1d188406
  NEW, PBA16-PLAIN db814168 x16
  @110003-18 (VPOS 9: b4+M8
  b6-9,76-79; b0 const db, b5
  const 5b; NO pair in tier).
- C10-1SIG single-sig EXACT map: e4492707
  x10 @110019-28 (VPOS 12: b4+M11
  b6-8,48-51,80-83; b5 const 5b; 10/10
  diverge).
- QUAD2s 2-sig 899c7472 x20 (cols 0-4) +
  8a9c7472 x44 (cols 5-15) col-split
  (VPOS 18: b0,b4,b5+QM7+R4+T4; b5
  step o>=51).
- T88-RING 06000000, 88B payload (VPOS
  17 = b4,b5+TM8+TR7 partition over
  0..87).
- Next P269 PB0 @110349+ (window
  TBD).

## 2. quad + T-ring?
- Quad split-b0 FIRST in quad: b0 = 89
  iff col<5 else 8a (5+11 per row x4
  rows, col-pure rule staged by m).
- Quad QM7 b9-11,76-79 shared 16/16 x3
  vs row0; NO frags (all positions
  COL-pure or ROW-pure, 0 MIXED).
- R4 b6,7,48,50 (b49-skipped const 5a)
  r1==r2==r3 LAST3-PAIRED 2/4 EXACT
  (r123 c5dec599 x3; r0 6fcb8377
  distinct).
- Tails row-shared 4/4 distinct
  452ed3b4/b7e31656/dce31656/01e41656;
  r1/r2 share last 3B e31656 (r3
  shares last 2B 1656).
- M-tails 16/16 ALL NEW vs P267T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [8-10,19,80-83]
  by COL 16/16; TR7 [13-15,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col / b76-79 row; b84-87
  const e365abcd (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 110001..110348: 348/348
  exact (whole tier incl 88B cells)?
- Quad b4=(0x9b+2off)&FF 64/64;
  b5=0x5b+(off>=51) 64/64; edge
  110079->110080 ff/5b->01/5c (mid-row3
  o=50->51)?
- T88-ring b4=(0x1b+2off)&FF 256/256;
  b5=0x5c+(off>=115)+(off>=243) 256/256;
  edges 110207->110208 ff/5c->01/5d +
  110335->110336 ff/5d->01/5e?
- Consts ALL 4: PBA 75 (b5-const), C10
  72 (b5-const), quad 66 (b5-step),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
