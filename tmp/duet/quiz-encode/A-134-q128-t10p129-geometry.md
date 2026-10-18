# A-134 (Q-128): T10P129 P-head geometry — DERIVED

Bed: census N=61629..61720 own bed (.rav[12:-4]).
First-hand; P128-M re-derived 61309 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 61629 96B/80B sig ccf18e08 (=P128-PB0);
  PB1 61630 100B/84B fat sig 10000000
  (=P128-PB1); PBA 61631..61646 (16, 100B/84B
  sig 7f010000 NEW); SINGLETON 61647 100B/84B
  sig 07000000 (=P123-PB1-fat); PBB9 61648..
  61656 (9, 100B/84B sig 05000000, 5th 100B
  PBB); QUAD 61657..61720 (64=4x16, ALL
  100B/84B, SINGLE sig 55000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,48,49,50,76-79] exact (b5 const 0xe1);
  PBB VPOS [4,44,45,46,47,49,50,51,80-83]
  exact (12B).

## 2. quad rows: CONFIRM
- M 6B pos[6,7,76,77,78,79] row-indep 16/16
  x4, full-tuple 16/16 distinct each row
  (heads b6,7 14/16 distinct pairs).
- R-band 7B b44,45,46,47,49,50,51 row-only:
  rows1==3 exact 284032dd707e37; row0
  888a14e5309c4f; row2 087422ed308247.
- Tails b80..83 row-const ALL distinct
  6ff771a1/04763adc/52f6a8e4/d6353edc.
- M-novelty vs P128M: ALL NEW (0/16 full, 0/16
  tails; 6B vs 7B layout). PBA M 7B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xe1 PBA/PBB; quad 0xe1->0xe2 step
  exactly at 61696.
- Quad varpos fully partitioned (counter+b5+
  R7+M6+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
