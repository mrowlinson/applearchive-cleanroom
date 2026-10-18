# A-328 (viewer r7): Q-328 T10P264 P-head @108609 — CONFIRM + 1 correction

First-hand bed 108609..109010 (qr7bed
extended; census RC=0 missing=0) +
P263T ref 108353..68 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 a2560300 NEW, PB1 bdcfaa06 NEW,
  PBA16-PLAIN e0932f72 x16 @108611-26
  (VPOS 9 exact b4+M8 b21-23,31,76-79;
  b0 const e0, b5 const 50; NO pair in
  tier).
- C10-1SIG bdcfaa06 x10 @108627-36
  (head-sig == PB1 sig ✓; VPOS 13 exact
  b4+M12 b22,23,30-35,80-83; b5 const
  50; 10/10 diverge).
- QUAD1s 1-sig e0932f72 x64 (VPOS 19
  exact b4,b5+QM7+F6+T4; b5 step
  o>=35 ✓; R7 const-folded out of
  VPOS ✓ — see correction).
- T88-NONSTD 06000000, 88B payload all
  256 ✓ (VPOS 18 exact b4,b5+TM9+TR7
  partition over 0..87; NONSTD M/R
  layout ✓).
- Next P265 PB0 @108957 a0560300 NEW +
  108958 bdcfaa06 (==P264PB1/B10) +
  PBA e0932f72 x16 @108959-74 (==P264
  PBA/QUAD) + B10 bdcfaa06 @108975+
  (window resolved; repeat-forward).

## 2. quad + T-ring: CONFIRM
- Quad QM7 b36-38,76-79 shared 16/16 x3
  vs row0.
- F6 row-frags b22/23/30/32/33/34: all
  six ADD rules 64/64 AND all six XOR
  rules 64/64 — TIE x6 CONFIRMED
  first-hand (all r1==r2 mid-paired ✓;
  staged ADD by nearest-family
  precedent b31-ADD P229 / b19-ADD
  P231/P239/P263 stands flagged).
- R7 sig-led b0-3,16-18 1/4 R-LESS
  EXACT: e0932f7204808d singleton in
  all 4 rows AND across all 64 cells
  (R7 all64 = 1 value; FIRST R-less
  quad, QRx4-identical + uniform
  handler staged ✓).
- Tails row-shared 4/4 distinct
  c37be99d/c0fadb1d/e5fadb1d/cb6a97b8
  EXACT; r1/r2 share last 3B fadb1d.
- M-tails 16/16 ALL NEW vs P263T (row-0
  reference, true novelty).
- T88-ring NONSTD: TM9 [18,19,39,46,47,
  80-83] by COL 16/16; TR7 [40-42,76-79]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b80-83 col / b76-79 row;
  b84-87 const f36a97b8 EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM + CORRECTION, NONE
- Odd-lencode ALL 108609..108956: 348/348
  exact (whole tier incl 88B cells).
- Quad b4=(0xbb+2off)&FF 64/64;
  b5=0x50+(off>=35) 64/64; edge
  108671->108672 ff/50->01/51 (mid-row2
  o=34->35 ✓).
- T88-ring b4=(0x3b+2off)&FF 256/256;
  b5=0x51+(off>=99)+(off>=227) 256/256;
  edges 108799->108800 ff/51->01/52 +
  108927->108928 ff/52->01/53.
- CORRECTION — quad consts: claimed 58
  (b5-step), first-hand 65. Derivation:
  quad VPOS is exactly the 19 staged
  positions (b4,b5+QM7+F6+T4, verified
  len 19); R7 contributes ZERO varpos
  (all64 singleton e0932f7204808d, so
  const-folded out of VPOS is correct);
  consts = 84-19 = 65. The staged 58
  (=84-19-7) double-subtracts the
  already-const R7. All other consts
  EXACT: PBA 75, C10 71, T88 70.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs (1 const-count correction: quad 65 not 58)
