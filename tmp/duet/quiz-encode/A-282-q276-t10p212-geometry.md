# A-282 (viewer r3): Q-276 T10P212 P-head @90513 — CONFIRM + CORRECTION

First-hand bed 90513..90876 (q276.py new;
census 90529..90876 RC=0 missing=0).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 f0070000
  REPEAT x3, PB1 e96d0f00 (==P211PB1),
  PBA 96def600 NEW (VPOS 7 exact b4+M6
  b6,7,76-79, b5 const c3).
- PBB10 f2961000 NEW single-sig (VPOS 11
  exact b4+M10 b6,7,48-51,80-83, b5
  const c3, 10/10 diverge; NO pair/C8 —
  direct PBA->PBB10->QUAD).
- QUAD 986e0901 NEW (VPOS 18 exact
  b4+M7+R10, b5 const c3).
- T-RING b8e99610 NEW (VPOS 16 exact =
  b4,b5+M7+R7 partition).
- Next @90861 4b080000 NEW (f007 run
  ends) + 90862 837b1300 NEW + 90863/64
  837b0b01 NEW.

## 2. quad + T-ring: CONFIRM + R-pair fix
- Quad M7 b9-11,76-79 shared 16/16 x3 vs
  row0 (== ring-ROW positions 7/7: QM==TR
  double link with B10M==QR 10/10, both
  set-exact).
- CORRECTION: R6 b6,7,48-51 is r0==r3
  PAIRED (8437e05f6425 both; 3/4
  distinct: r1 7e4450dfa98b, r2
  664b26de2d57) — NOT unpaired 4/4.
- Tails row-shared 4/4 distinct
  2ada5b52/0724baa4/f2a46950/15a68cec
  EXACT (r0/r3 share R, differ tails).
- M-tails 16/16 ALL NEW vs P211T rows
  (col-0 row reference, true novelty).
- T-ring ROLE-SWAP2: M7 [16-18,72-75] by
  COL 16/16; R7 [9-11,76-79] by ROW
  16/16; transpose-swapped exact; tails
  const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 90513..90860: 348/348
  exact (whole tier).
- T-ring b4=(0xdb+2off)&FF 256/256;
  b5=0xc3+(off>=19)+(off>=147) 256/256;
  edges 90623->90624 ff/c3->01/c4 +
  90751->90752 ff/c4->01/c5.
- Consts ALL 4 EXACT: PBA 77 (b5-const
  ✓), PBB 73 (b5-const ✓), quad 66
  (b5-const ✓), T 68.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; R6 r0==r3 paired (not 4/4)
