# Q-309 (writer2 s20): T10P245 P-head @101997 — geometry?

Own first-hand bed 101997..102344 (census RC=0
missing=0), staged p245-patch.txt, sweep
348/348 err 0 (try-p245; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 d46f0100 NEW, PB1 b553d702
  NEW, PBA 2085c72e NEW (VPOS 7:
  b4+M6 b24,25,76-79; b5 const 1c;
  NO pair in tier).
- C10-2SIG EXACT map: 7d38be05 x3
  @102015-17 + 7d38de02 x7 @102018-24
  (VPOS 19: b4,b5+M17 b2,3,21-31,80-83;
  b5-CARRY 1c->1d @102015->102016
  ff->01 edge INSIDE block; 10/10
  diverge).
- QUAD 2085c72e x64 (==PBA sig; VPOS
  20: b4+QM8+R7+T4; b5 const 1d).
- T88-RING 02000000 (==P242/243/244T
  sig), 88B payload (VPOS 17 =
  b4,b5+TM7+TR8 partition over 0..87).
- Next P246 PB0 @102345+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM8 b21-23,31,76-79 shared
  16/16 x3 vs row0 (clean, no b42).
- R7 b24-30 r1==r2==r3 TRIPLE 2/4
  EXACT (ba7c80a31478a7 x3; r0
  933cc422d4f27c distinct).
- Tails row-shared 4/4 distinct
  c26f98d7/78214c1b/a2214c1b/cc214c1b;
  r1/r2/r3 share last 3B 214c1b
  (matching R-triple).
- M-tails 16/16 ALL NEW vs P244T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [40-42,76-79]
  by COL 16/16 (b42 in T-M); TR8
  [25-27,35,80-83] by ROW 16/16
  UNPAIRED (16 distinct); tails SPLIT
  b76-79 col / b80-83 row; b84-87 const
  b196ffe1 (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 101997..102344: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0x93+2off)&FF 256/256;
  b5=0x1d+(off>=55)+(off>=183) 256/256;
  edges 102143->102144 ff/1d->01/1e +
  102271->102272 ff/1e->01/1f?
- Consts ALL 4: PBA 77 (b5-const), C10
  65 (b5-carry), quad 64 (b5-const),
  T88 71 (88-17)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
