# A-343 (viewer r8): Q-343 T10P279 P-head @113829 — CONFIRM all 3

First-hand bed 113829..114176 (qr8bed own
oracle runs; census RC=0 missing=0) +
P278T ref 113573..88 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b8aa0700 NEW, PB1 74b05c0f NEW,
  PBA16-SPLIT12/4 c605cbf5 x12
  @113831-42 + c805cbf5 x4 @113843-46
  EXACT split (VPOS 9 exact
  b0,b4+M7 b9-11,76-79; b5 const 79;
  16/16 distinct, NO pair in tier).
- C10-1SIG 5eb05c0f x10 @113847-56
  (VPOS 12 exact b4+M11 b13-19,80-83;
  b5 const 79; 10/10 diverge).
- QUAD2s 2-sig a09b0ff6 x16 (row0) +
  00928ff4 x48 (rows1-3) EXACT
  row-split (VPOS 20 exact
  b4,b5+QM7+R7+T4; b5 step o>=63
  LAST-CELL ✓).
- T88-RING 0f000000, 88B payload all
  256 ✓ (VPOS 16 exact b4,b5+TM8+TR6
  partition over 0..87).
- Next P280 PB0 @114177 58ae0700 NEW +
  114178 2557520f NEW + PBA c09417fb
  x16 @114179-94 + C10 2557520f
  @114195+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b12,13,19,76-79 shared 16/16
  x3 vs row0; NO frags (0 MIXED ✓).
- R7 sig-led b0-3,16-18 r1==r2==r3
  LAST3-PAIRED 2/4 EXACT (r123
  00928ff4c51894 x3; r0 a09b0ff6f9d44c
  distinct).
- Tails row-shared 4/4 distinct
  9aa19575/7f90f0d4/a490f0d4/c990f0d4
  EXACT; r1/r2/r3 share last 3B 90f0d4
  (tails echo the R last3-pairing ✓).
- M-tails 16/16 ALL NEW vs P278T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM8 [28-31,80-83]
  by COL 16/16; TR6 [20,21,76-79] by
  ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const 75daa80b EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 113829..114176: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0x83+2off)&FF 64/64;
  b5=0x79+(off>=63) 64/64; edge
  113919->113920 ff/79->01/7a (LAST
  cell o=62->63 ✓).
- T88-ring b4=(0x03+2off)&FF 256/256;
  b5=0x7a+(off>=127)+(off>=255) 256/256;
  edges 114047->114048 ff/7a->01/7b +
  114175->114176 ff/7b->01/7c (2nd
  LAST-CELL o=254->255 ✓).
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 72 (b5-const), quad 64 (b5-step),
  T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
