# A-283 (viewer r3): Q-277 T10P213 P-head @90861 — CONFIRM + CORRECTION

First-hand bed 90861..91224 (q277.py new;
census 90877..91920 RC=0 missing=0).

## 1. shape: CONFIRM + VPOS fix
- 348 cells sizes {(100,84)}. PB0 4b080000
  NEW, PB1 837b1300 NEW, PBA 837b0b01 NEW
  (VPOS 9 exact b4+M8 b24-27,76-79, b5
  const c5).
- PBB10 8f9b1100 NEW single-sig (VPOS 15
  exact b4,b5+M13 b20,21,25-31,80-83;
  b5-carry c5->c6 @90879->90880 ff->01,
  first B-carry; 10/10 diverge; NO
  pair/C8).
- QUAD 8f9b0901 NEW (VPOS 20 exact
  b4+M8+R11, b5 const c6).
- T-RING d0cf4b1c NEW. CORRECTION: VPOS
  20 (not 18) = b4,b5+M8+R10 exact
  partition [4,5,14,15,21,22,23,31,32,
  37-39,72-79]; leg-3 consts 64 already
  implies 20 (84-20). Count stands.
- Next @91209 4b080000 REPEAT + 91210
  8f9b1100 (==P213B10sig) + 91211/12
  8f9b3d01 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M8 b32-35,76-79 shared 16/16 x3 vs
  row0.
- R7 b24-30 UNPAIRED 4/4 distinct.
- R-sharing 10/11 EXACT: shared
  25-30,80-83; quad-only b24; B-only
  b20,21,31.
- Tails row-shared 4/4 distinct
  4076c7ad/5774bc0b/bab1bb84/8d337c2f
  EXACT.
- M-tails 16/16 ALL NEW vs P212T rows
  (col-0 row reference, true novelty).
- T-ring STANDARD: M8 b32,37-39,76-79 by
  COL 16/16; R10 b14,15,21-23,31,72-75
  by ROW 16/16 UNPAIRED (16 distinct);
  tails const (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 90861..91208: 348/348
  exact (whole tier).
- T-ring b4=(0x93+2off)&FF 256/256;
  b5=0xc6+(off>=55)+(off>=183) 256/256;
  edges 91007->91008 ff/c6->01/c7 +
  91135->91136 ff/c7->01/c8.
- Consts ALL 4 EXACT: PBA 75 (b5-const
  ✓), PBB 69 (b5-carry ✓), quad 64
  (b5-const ✓), T 64.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees; T-ring VPOS 20 (not 18)
