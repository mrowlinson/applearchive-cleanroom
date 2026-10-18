# A-150 (Q-144): T10P137 P-head geometry — DERIVED

Bed: census N=64413..64504 own bed (.rav[12:-4]).
First-hand; P136-M re-derived 64093 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 64413 96B/80B sig 14f352a2 NEW; PB1
  64414 100B/84B fat sig a7000000 (=P135-
  singleton); PBA 64415..64430 (16, 100B/84B
  sig e20b0000 NEW); SINGLETON 64431 100B/84B
  sig a6000000 NEW; PBB9 64432..64440 (9,
  100B/84B sig 76000000 NEW, 10th 100B PBB);
  QUAD 64441..64504 (64=4x16, ALL 100B/84B,
  SINGLE sig 65070000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,48,49,76-79] exact (b5 const 0xf7); PBB
  VPOS [4,44,45,46,47,49,50,51,80-83] exact
  (12B).

## 2. quad rows: CONFIRM (1st 0==3 pairing)
- M 8B pos[6,7,8,9,76,77,78,79] (7th 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b6-9 15/16 distinct quads).
- R-band 7B b44,45,46,47,49,50,51 row-only:
  rows0==3 exact 895b097960e45e; row1
  a9d88e4da0028f; row2 49bb8a8fe0daee.
- Tails b80..83 row-const d8f4d262/7ef7ab2d/
  99761fd9/b4f8d362 (rows0,3 differ b0 only).
- M-novelty vs P136M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 8B layout). PBA M 6B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xf7 PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R7+
  M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
