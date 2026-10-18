# A-301 (viewer r3): Q-295 T10P231 P-head @97125 — CONFIRM all 3

First-hand bed 97125..97488 (q295.py new,
88B-aware; census 97141..97488 RC=0
missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT (first mixed-size tier).
- PB0 329d0000 NEW, PB1 f1053b01 NEW, PBA
  2d5eb013 NEW (VPOS 8 exact b4+M7
  b9-11,76-79, b5 const f6).
- PBB10 e0053b01 NEW single-sig (VPOS 13
  exact b4,b5+M11 b13-19,80-83; b5-carry
  f6->f7 @97151->97152 ff->01 edge;
  10/10 diverge; NO pair/C8).
- QUADms 15 sigs EXACT in column order
  (d33d/d63d/d73d/dd3d x2 cols 3-4/a895/
  aa95/ae95/b095/b295/b895/b78d/b88d/
  bd8d/be8d/c18d; full 4B ..6e1e/..961e;
  VPOS 20 exact b4+M8+R6+b19+T4, b5
  const f7 single-valued).
- T88-RING 01000000 NEW, 88B payload
  (104,88) all 256 ✓ (VPOS 18 exact =
  b4,b5+M7+R9 partition over 0..87).
- Next @97473 053b0100 NEW + 97474
  dd1a3f01 NEW + PBA 2-sig: 97475..97482
  dd1adf14 x8 + 97483.. dd1a2f16 (x6
  probed, continues past census).

## 2. quad + T-ring: CONFIRM
- Quad M8 b0-2,11,76-79 shared 16/16 x3 vs
  row0 (sig-led cols = the 15 tags ✓).
- b19: ADD A=[0,9,9,-11] 64/64 ✓ AND XOR
  X=[00,0b,0b,1f] 64/64 ✓ — BOTH FIT
  first-hand (M19 col-vector 2-valued
  0x35/0xb5 ✓; r1==r2 rows ✓; r3 -11 ✓).
  VERDICT: genuinely undecidable from
  this tier (+9≡^0x0b and -11≡^0x1f on
  {0x35,0xb5} — verified arithmetically);
  staged ADD stands by b31 precedent;
  tie-break needs M19 lows ≥7 (e.g. 0x37:
  +9=0x40 vs ^0x0b=0x3c). No XOR
  preference derivable — flag as tie,
  not miss.
- R6 b13-18 r1==r2 PAIRED 3/4 EXACT
  (b2fc01da137e x2; r0/r3 distinct).
- Tails row-shared 4/4 distinct
  2738643c/d7ecaf3d/01edaf3d/4beeaca6
  EXACT; r1/r2 share last 2B af3d ✓
  (matching R-pair).
- M-tails 16/16 ALL NEW vs P230T (row-0
  reference, true novelty).
- T88-ring STANDARD: M7 [29-31,80-83] by
  COL 16/16; R9 [16-19,23,76-79] by ROW
  16/16 UNPAIRED (16 distinct); tails
  SPLIT b80-83 col (16) / b76-79 row
  (16); b84-87 const (d6/38/64/3c
  single-valued ✓ — 88B tail layout as
  speculated).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 97125..97472: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x83+2off)&FF 256/256;
  b5=0xf7+(off>=63)+(off>=191) 256/256;
  edges 97279->97280 ff/f7->01/f8 +
  97407->97408 ff/f8->01/f9.
- Consts ALL 4 EXACT (fixed rule
  verified): PBA 76 (b5-const ✓), PBB 71
  (b5 varies carry ✓), quad 64 (b5-const
  ✓), T88 70 (88-18 ✓ new denominator).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
