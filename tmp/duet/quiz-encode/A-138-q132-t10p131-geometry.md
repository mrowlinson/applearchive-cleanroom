# A-138 (Q-132): T10P131 P-head geometry — DERIVED

Bed: census N=62325..62416 own bed (.rav[12:-4]).
First-hand; P130-M re-derived 62005 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 62325 96B/80B sig e0f3c00a NEW; PB1
  62326 100B/84B fat sig 12000000 NEW (1st 12
  fat); PBA 62327..62342 (16, 100B/84B sig
  a8010000 NEW); SINGLETON 62343 100B/84B sig
  12000000 (=PB1); PBB9 62344..62352 (9,
  100B/84B sig 09000000, 6th 100B PBB); QUAD
  62353..62416 (64=4x16, ALL 100B/84B, SINGLE
  sig 92000000 =P130-quad-sig).
- 1x96B + 91x100B exact. PBA VPOS
  [4,5,32,33,38,39,76-79] exact (b5 0xe6->0xe7
  @62336, 2nd intra-PBA step); PBB VPOS
  [4,29,30,31,37,38,39,40,41,42,80-83] exact
  (14B).

## 2. quad rows: CONFIRM
- M 8B pos[44,45,46,47,76,77,78,79] (3rd 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b44-47 15/16 distinct quads).
- R-band 8B b29,30,31,38,39,40,41,42 row-only,
  ALL 4 distinct: bf8901e62d2df0be/7f150f15
  efedc9be/7fc81d646ecd03bf/ff421308eecddcbe.
- b37 const (0x85) in quad.
- Tails b80..83 row-const ALL distinct
  4f32d195/10f73810/e836421e/69ed1777.
- M-novelty vs P130M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 6B layout). PBA M 8B 16/16;
  PBB M 13B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 0xe6->0xe7 step @62336 (PBA), const 0xe7
  PBB/quad.
- Quad varpos fully partitioned (counter+R8+
  M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
