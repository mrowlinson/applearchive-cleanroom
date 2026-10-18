# A-341 (viewer r8): Q-341 T10P277 P-head @113133 — CONFIRM all 3

First-hand bed 113133..113480 (qr8bed own
oracle runs; census RC=0 missing=0) +
P276T ref 112877..92 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 b6aa0700 NEW, PB1 d505540f NEW,
  PBA16-PLAIN e09a1ffa x16 @113135-50
  (VPOS 9 exact b4+M8 b24-27,76-79;
  b0 const e0, b5 const 73; 16/16
  distinct, NO pair in tier).
- C10-CARRY f5f4570f x10 @113151-60
  (VPOS 14 exact b4,b5+M12
  b24-31,80-83; b5 73+step1; 10/10
  diverge).
- QUAD1s 1-sig e09a1ffa x64 (VPOS 20
  exact b4+QM8+R7+T4; b5 const 74).
- T88-ROWTAIL 08000000, 88B payload all
  256 ✓ (VPOS 17 exact
  b4,b5+TM8+TR3+TT4 partition over
  0..87; tails ROW-led not col-split).
- Next P278 PB0 @113481 b0aa0700 NEW +
  113482 f5f4570f (==P277C10sig) + PBA
  e09a1ffa x16 @113483-98 + C10
  f5f4570f @113499+ (window resolved).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b21-23,31,76-79 shared 16/16
  x3 vs row0; NO frags (0 MIXED ✓).
- R7 b24-30 r1==r2==r3 LAST3-PAIRED 2/4
  EXACT (r123 cb3c329115c98d x3; r0
  acbca4ea955e68 distinct).
- Tails row-shared 4/4 distinct
  0b6db88f/b3dff5e9/246311ea/8a1ff0ea
  EXACT; no shared suffix >= 2B ✓
  (last-2B b88f/f5e9/11ea/f0ea all
  distinct; only r2/r3 share last 1B
  ea).
- M-tails 16/16 ALL NEW vs P276T (row-0
  reference, true novelty).
- T88-ring ROWTAIL: TM8 [40-43,76-79]
  by COL 16/16; TR3 [29,34,35] by ROW
  14/16 EXACT (r6==r7 fe4de6 +
  r14==r15 ff6d87 shared ✓; tails
  disambiguate); tails b80-83 ROW-led
  16/16 (staged _T10P277TT by q, 3rd
  rowtail T88 ✓); b84-87 const
  2783811e EXACT (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 113133..113480: 348/348
  exact (whole tier incl 88B cells).
- C10 b4=(0xff+2off)&FF 10/10;
  b5=0x73+(off>=1) 10/10; edge
  113151->113152 ff/73->01/74
  (first-cell carry o=0->1 ✓).
- T88-ring b4=(0x93+2off)&FF 256/256;
  b5=0x74+(off>=55)+(off>=183) 256/256;
  edges 113279->113280 ff/74->01/75 +
  113407->113408 ff/75->01/76.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  C10 70 (b5-step), quad 64 (b5-const),
  T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
