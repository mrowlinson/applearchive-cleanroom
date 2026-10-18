# A-342 (viewer r8): Q-342 T10P278 P-head @113481 — CONFIRM all 3

First-hand bed 113481..113828 (qr8bed own
oracle runs; census RC=0 missing=0) +
P277T ref 113225..40 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b0aa0700 NEW, PB1 f5f4570f
  SAME-as-P277C10sig ✓ (byte-equal to
  n113151 first-hand), PBA16-PLAIN
  e09a1ffa x16 @113483-98 (VPOS 9
  exact b4+M8 b34,35,42,43,76-79; b0
  const e0, b5 const 76; 16/16
  distinct, NO pair in tier).
- C10-1SIG f5f4570f x10 @113499-508
  (VPOS 14 exact b4+M13
  b34,35,41-47,80-83; b5 const 76;
  10/10 diverge; head-sig == PB1
  sig ✓).
- QUAD1s 1-sig e09a1ffa x64 (VPOS 19
  exact b4,b5+QM6+R7+T4; b5 step
  o>=27).
- T88-ROWTAIL 0f000000, 88B payload all
  256 ✓ (VPOS 16 exact
  b4,b5+TM8+TR2+TT4 partition over
  0..87; tails ROW-led not col-split).
- Next P279 PB0 @113829 b8aa0700 NEW +
  113830 74b05c0f NEW + PBA split
  c605cbf5 x12 + c805cbf5 x4
  @113831-46 + C10 5eb05c0f @113847+
  (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM6 b48,49,76-79 shared 16/16 x3
  vs row0; NO frags (0 MIXED ✓).
- R7 b34,35,42-46 (b47-skipped const
  96 ✓) r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 333104ef5407a6 x3; r0
  a551220fd42f94 distinct).
- Tails row-shared 4/4 distinct
  18e71aa7/1eef163c/8eae4f3c/b3ae4f3c
  EXACT; r2/r3 share last 3B ae4f3c ✓.
- M-tails 16/16 ALL NEW vs P277T (row-0
  reference, true novelty).
- T88-ring ROWTAIL: TM8 [6,7,12,13,76-79]
  by COL 16/16; TR2 [52,53] by ROW
  15/16 EXACT (r6==r7 f1d5 shared ✓;
  tails disambiguate); tails b80-83
  ROW-led 16/16 (staged _T10P278TT by
  q, 4th rowtail T88 ✓); b84-87 const
  7f5fc217 EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 113481..113828: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xcb+2off)&FF 64/64;
  b5=0x76+(off>=27) 64/64; edge
  113535->113536 ff/76->01/77 (mid-row1
  o=26->27 ✓).
- T88-ring b4=(0x4b+2off)&FF 256/256;
  b5=0x77+(off>=91)+(off>=219) 256/256;
  edges 113663->113664 ff/77->01/78 +
  113791->113792 ff/78->01/79.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 70 (b5-const), quad 65 (b5-step),
  T88 72 (88-16).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
