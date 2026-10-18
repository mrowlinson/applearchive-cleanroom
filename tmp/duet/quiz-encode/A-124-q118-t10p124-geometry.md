# A-124 (Q-118): T10P124 P-head geometry — DERIVED

Bed: census N=59889..59980 own bed (.rav[12:-4]).
First-hand; P123-M re-derived 59569 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 59889 96B/80B sig f6782402 (=P123-PB0);
  PB1 59890 100B/84B fat sig 05000000 NEW (1st
  05 fat); PBA 59891..59906 (16, 100B/84B sig
  57000000 NEW); NO extra singleton; PBB10
  59907..59916 (10, 100B/84B sig 04000000
  =P119-PB1-fat); QUAD 59917..59980 (64=4x16,
  ALL 100B/84B, SINGLE sig 54000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,5,6,7,76-79] exact (b5 steps @59904, 1st
  intra-PBA step -- values CORRECTED leg3);
  PBB VPOS [4,6,7,12,13,14,15,80-83] exact
  (11B).

## 2. quad rows: CONFIRM
- M 7B pos[13,14,15,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b13,14,15 15/16 distinct triples).
- R-band 6B b6,7,8,9,10,11 row-only:
  rows1==3 exact 98dc1cc81456; row0
  3b5a7c0c2f5c; row2 4add9c9f6962.
- Tails b80..83 row-const ALL distinct
  83c688d4/06609d26/18941dc5/2255d7de.
- M-novelty vs P123M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 7B layout). PBA M 6B 16/16;
  PBB M 10B 10/10.

## 3. counters + dips: CORRECT b5 (off-by-2), else CONFIRM
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 0xd3->0xd4 step @59904 (PBA), const 0xd4
  PBB/quad -- NOT 0xd1->0xd2/0xd2. Counter
  formula forces it (n=59891 -> 0xd3; step at
  b4 wrap 59904); R121/R122 bases (0xd1+2 /
  0xd4) bracket consistently.
- Quad varpos fully partitioned (counter+R6+
  M7+tails), 0 stragglers. NO D-class dips.

## legs 1-2 agree; leg3 CORRECTS b5 values
