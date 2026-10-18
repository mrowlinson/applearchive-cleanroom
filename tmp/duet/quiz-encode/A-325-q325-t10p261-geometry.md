# A-325 (viewer r7): Q-325 T10P261 P-head @107565 — CONFIRM all 3

First-hand bed 107565..107960 (qr7bed
extended; census RC=0 missing=0) +
P260T ref 107309..24 (own bed).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84) x92, (104,88)
  x256} EXACT.
- PB0 0f550300 NEW, PB1 adecad06 NEW,
  PBA e08ad76e x16 NEW (VPOS 9 exact
  b4+M8 b24-27,76-79; b5 const 48; NO
  pair in tier).
- B10 single-sig 35fda506 x10 (VPOS 13
  exact b4+M12 b24-31,80-83; b5 const
  48; 10/10 diverge).
- QUAD e08ad76e x64 (==PBA sig ✓; VPOS
  21 exact b4,b5+QM8+R7+T4; b5-carry
  48->49 @107647->107648 ff->01 edge).
- T88-RING 06000000 (==P252/253/256/
  259T sig), 88B payload all 256 ✓
  (VPOS 17 exact b4,b5+TM7+TR8
  partition over 0..87).
- Next P262 PB0 @107913 0a550300 NEW +
  107914 35fda506 (==P261B10 sig) +
  PBA e08ad76e x16 @107915-30 (==P261
  PBA/QUAD sig) + B10 35fda506
  @107931+ (window resolved; heavy
  repeat-forward).

## 2. quad + T-ring: CONFIRM
- Quad QM8 b21-23,31,76-79 shared
  16/16 x3 vs row0.
- R7 b24-30 r0==r2 EVEN-PAIRED 3/4
  EXACT (e53cf3d4b53eb1 x2; r1
  5f3c623315b6d1 + r3 f6bcd40cf5d63e
  distinct — first EVEN r02 pair ✓).
- Tails row-shared 4/4 distinct
  7fa0e666/9517fb30/caa0e666/027177fa
  EXACT; r0/r2 share last 3B a0e666
  (matching R-pair ✓).
- M-tails 16/16 ALL NEW vs P260T (row-0
  reference, true novelty).
- T88-ring STANDARD: TM7 [40-42,76-79]
  by COL 16/16; TR8 [25-27,35,80-83]
  by ROW 16/16 UNPAIRED (16 distinct);
  tails SPLIT b76-79 col / b80-83 row;
  b84-87 const 22ecf42b EXACT
  (1 ring-wide).

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode ALL 107565..107912: 348/348
  exact (whole tier incl 88B cells).
- T88-ring b4=(0x13+2off)&FF 256/256;
  b5=0x49+(off>=119)+(off>=247) 256/256;
  edges 107775->107776 ff/49->01/4a +
  107903->107904 ff/4a->01/4b.
- Consts ALL 4 EXACT: PBA 75 (b5-const),
  B10 71 (b5-const), quad 63 (b5 varies
  carry), T88 71 (88-17).
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
