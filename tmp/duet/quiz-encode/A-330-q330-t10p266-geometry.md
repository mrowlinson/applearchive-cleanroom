# A-330 (viewer r7): Q-330 T10P266 P-head @109305 — CONFIRM all 3

First-hand bed 109305..109700 (qr7bed
extended; census RC=0 missing=0) +
P265T ref 109049..64 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 a0740300 NEW, PB1 2a40e906 NEW,
  PBA16-CARRY 8087f776 x16 @109307-22
  (VPOS 11 exact b4,b5+M9 b12-15,19,
  76-79; b0 const 80, b5 55+step5; NO
  pair in tier).
- C10-5SIG map EXACT: 958dec06 x5
  @109323-27 + e5e87b03/dd767803/
  6d417603/750e7e03 x2 @109328-32 (5
  distinct ✓; VPOS 16 exact b4+M15
  b0-3,11,18-23,80-83; b5 const 56;
  10/10 diverge).
- QUAD1s 1-sig c0822772 x64 (VPOS 20
  exact b4+QM7+R8+T4; b5 const 56).
- T88-RING 03000000, 88B payload all
  256 ✓ (VPOS 16 exact b4,b5+TM7+TR7
  partition over 0..87).
- Next P267 PB0 @109653 a0740300
  (==P266PB0 REPEAT) + 109654 1d18e406
  NEW + PBA c0822772 x16 @109655-70
  (==P266QUAD sig) + B10 1d18e406
  @109671+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b24-26,76-79 shared 16/16 x3
  vs row0; NO frags (all payload
  positions COL-pure or ROW-pure, 0
  MIXED — b4 counter excluded as
  usual).
- R8 b12-14,18-22 r0==r3 AND r1==r2
  DOUBLE-PAIRED 2/4 EXACT (r03
  f216dbb97b532400 x2; r12
  32999dc175931007 x2; FIRST
  double-paired quad: EVEN + MID
  together ✓).
- Tails row-shared 4/4 distinct
  b3327d33/ceb7d61f/f3b7d61f/23337d33
  EXACT; r1/r2 share last 3B b7d61f +
  r0/r3 share last 2B 7d33 (tails echo
  the R double-pairing ✓).
- M-tails 16/16 ALL NEW vs P265T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [27,34,35,80-83]
  by COL 16/16; TR7 [28-30,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const 28ee7163 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 109305..109652: 348/348
  exact (whole tier incl 88B cells).
- PBA b4=(0xf7+2off)&FF 16/16;
  b5=0x55+(off>=5) 16/16; edge
  109311->109312 ff/55->01/56.
- T88-ring b4=(0xab+2off)&FF 256/256;
  b5=0x56+(off>=43)+(off>=171) 256/256;
  edges 109439->109440 ff/56->01/57 +
  109567->109568 ff/57->01/58.
- Consts ALL 4 EXACT: PBA 73 (b5-step),
  C10 68 (b5-const), quad 64 (b5-const),
  T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
