# A-338 (viewer r8): Q-338 T10P274 P-head @112089 — CONFIRM all 3

First-hand bed 112089..112436 (qr8bed own
oracle runs; census RC=0 missing=0) +
P273T ref 111833..48 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b2690700 NEW, PB1 1e65d30e NEW,
  PBA16-PLAIN e09effe0 x16 @112091-106
  (VPOS 9 exact b4+M8 b12-14,19,76-79;
  b0 const e0, b5 const 6b; 16/16
  distinct, NO pair in tier).
- C10-5SIG EXACT map first-hand:
  2557da0e x5 @112107-11 + a53dd90e
  @112112 + a5eb6b07 @112113 +
  adcd6607 @112114 + 7541d50e x2
  @112115-16 (VPOS 16 exact b4+M15
  b0-3,11,18-23,80-83; b5 const 6b;
  10/10 diverge).
- QUAD1s 1-sig 809907fc x64 (VPOS 19
  exact b4,b5+QM6+R7+T4; b5 step
  o>=11).
- T88-SPLIT 0e/0f (160+96), 88B payload
  all 256 ✓ (VPOS 19 exact
  b0,b4,b5+TM10+TR6 partition over
  0..87).
- Next P275 PB0 @112437 b2690700
  (==P274PB0) + 112438 0d2bd60e NEW +
  PBA 809907fc x16 @112439-54 +
  C10-2SIG 0d2bd60e x5 + 0d2b6607 x5
  @112455-64 (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM6 b24,25,76-79 shared 16/16 x3
  vs row0; NO frags (0 MIXED ✓).
- R7 b13,14,18-22 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  e986627793551a x3; r0 5ad7e27b73e712
  distinct).
- Tails row-shared 4/4 distinct
  30f07a3b/13f4bcdf/38f4bcdf/5df4bcdf
  EXACT; r1/r2/r3 share last 3B f4bcdf
  (tails echo the R last3-pairing ✓).
- M-tails 16/16 ALL NEW vs P273T (row-0
  reference, true novelty).
- T88-ring SPLIT-b0: TM10
  [11,18,19,27,34,35,80-83] by COL
  16/16; TR6 [28,29,76-79] by ROW
  16/16 UNPAIRED (16 distinct); b0 =
  0e iff col<10 else 0f, 256/256
  EXACT (10+6 per row x16 rows); tails
  SPLIT b80-83 col / b76-79 row;
  b84-87 const c229ac4d EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 112089..112436: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xeb+2off)&FF 64/64;
  b5=0x6b+(off>=11) 64/64; edge
  112127->112128 ff/6b->01/6c (mid-row0
  o=10->11 ✓).
- T88-ring b4=(0x6b+2off)&FF 256/256;
  b5=0x6c+(off>=75)+(off>=203) 256/256;
  edges 112255->112256 ff/6c->01/6d +
  112383->112384 ff/6d->01/6e.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 68 (b5-const), quad 65 (b5-step
  = 84-19 ✓ per A-328 rule), T88 69
  (88-19).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
