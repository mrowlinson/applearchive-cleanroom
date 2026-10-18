# A-340 (viewer r8): Q-340 T10P276 P-head @112785 — CONFIRM all 3

First-hand bed 112785..113132 (qr8bed own
oracle runs; census RC=0 missing=0) +
P275T ref 112529..44 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b6690700 NEW, PB1 0d2b660e NEW,
  PBA16-PLAIN ddb062e6 x16 @112787-802
  (VPOS 8 exact b4+M7 b6,7,9,76-79
  b8-skipped const dc ✓; b0 const dd,
  b5 const 71; 16/16 distinct, NO pair
  in tier).
- C10-1SIG 386c550f x10 @112803-12
  (VPOS 12 exact b4+M11
  b6-8,48-51,80-83; b5 const 71;
  10/10 diverge).
- QUAD2s 2-sig col-split c1c356f5 x52
  (cols 0-12) + e4c356f5 x12 (cols
  13-15) EXACT (VPOS 21 exact
  b0,b4+QM9+R6+T4; b5 const 71).
- T88-FRAG 0e000000, 88B payload all
  256 ✓ (VPOS 20 exact
  b4,b5+TM8+b8+TR9 partition over
  0..87; FIRST T88 row-frag ✓).
- Next P277 PB0 @113133 b6aa0700 NEW +
  113134 d505540f NEW + PBA e09a1ffa
  x16 @113135-50 + C10 f5f4570f
  @113151+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad split-b0 2nd in quad: b0 = c1
  iff col<13 else e4, 64/64 EXACT
  (13+3 per row x4 rows, col-pure rule
  staged by m ✓).
- Quad QM9 b9-13,76-79 shared 16/16 x3
  vs row0; NO frags (0 MIXED ✓).
- R6 b6-8,48,50,51 (b49-skipped const
  df ✓) r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 31142182fe5d x3; r0
  73ff014fe862 distinct).
- Tails row-shared 4/4 distinct
  f6592f08/8da3a08d/b2a3a08d/d7a3a08d
  EXACT; r1/r2/r3 share last 3B a3a08d
  (tails echo the R last3-pairing ✓).
- M-tails 16/16 ALL NEW vs P275T (row-0
  reference, true novelty).
- T88-ring FRAG: TM8 [9-11,19,80-83]
  by COL 16/16; b8 row-XOR X=[00x13,
  20,20,20] 256/256 AND row-ADD A=
  [0x13,32,32,32] 256/256 — TIE
  CONFIRMED first-hand (rows 13-15
  last-three-equal shape = X42-family
  ✓; staged XOR by X42 shape
  precedent stands flagged); TR9
  [13-17,76-79] by ROW 16/16 UNPAIRED;
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const 2c295916 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 112785..113132: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0xdb+2off)&FF 256/256;
  b5=0x71+(off>=19)+(off>=147) 256/256;
  edges 112895->112896 ff/71->01/72 +
  113023->113024 ff/72->01/73.
- Consts ALL 4 EXACT: PBA 76 (b5-const),
  C10 72 (b5-const), quad 63 (b5-const),
  T88 68 (88-20).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
