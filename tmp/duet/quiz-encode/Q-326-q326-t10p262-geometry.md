# Q-326 (writer2 s20): T10P262 P-head @107913 — geometry?

Own first-hand bed 107913..108260 (census RC=0
missing=0), staged p262-patch.txt, sweep
348/348 err 0 (try-p262; 88B allowlist
carried).

## 1. shape?
- 348 cells sizes {(100,84) x92, (104,88)
  x256}. PB0 0a550300 NEW, PB1 35fda506
  (==P261B10), PBA e08ad76e x16
  (==P261PBA sig; VPOS 10: b4+M9
  b15,34,35,42,43,76-79; b5 const 4b;
  NO pair in tier).
- C10-2SIG sandwich EXACT map: 35fda506
  x5 @107931-35 + 35fd5503 x1 @107936 +
  35fda506 x4 @107937-40 (VPOS 16:
  b4+M15 b2,3,34,35,41-47,80-83; b5
  const 4b; 10/10 diverge).
- QUAD e08ad76e x64 (==PBA sig; VPOS
  19: b4+QM6+R8+T4; b5 const 4b).
- T88-RING 06000000, 88B payload (VPOS
  14 = b4,b5+TM6+TR6 partition over
  0..87 — smallest T yet).
- Next P263 PB0 @108261+ (window
  TBD).

## 2. quad + T-ring?
- Quad QM6 b48,49,76-79 shared 16/16 x3
  vs row0.
- R8 b34,35,41-46 r1==r2 PAIRED 3/4
  EXACT (68083c92d7d4a24c x2; r0
  c408fc9f5754253d + r3 c822bc9ecf948f06
  distinct).
- Tails row-shared 4/4 distinct
  928e9d33/bdc02fdf/e2c02fdf/734a4841;
  r1/r2 share last 3B c02fdf (matching
  R-pair).
- M-tails 16/16 ALL NEW vs P261T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM6 [6,7,76-79] by
  COL 16/16; TR6 [52,53,80-83] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b76-79 col / b80-83 row; b84-87
  const 670865ca (1 ring-wide).

## 3. counters + dips?
- Odd-lencode ALL 107913..108260: 348/348
  exact (whole tier incl 88B cells)?
- T88-ring b4=(0xcb+2off)&FF 256/256;
  b5=0x4b+(off>=27)+(off>=155) 256/256;
  edges 108031->108032 ff/4b->01/4c +
  108159->108160 ff/4c->01/4d?
- Consts ALL 4: PBA 74 (b5-const), C10
  68 (b5-const), quad 65 (b5-const),
  T88 74 (88-14)?
- varpos partitioned exact, 0 stragglers?
  D-class dips?
