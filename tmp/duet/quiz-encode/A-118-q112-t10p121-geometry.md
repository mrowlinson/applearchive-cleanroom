# A-118 (Q-112): T10P121 P-head geometry — DERIVED

Bed: census N=58845..58936 own bed (.rav[12:-4]).
First-hand; P120-M re-derived 58525 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 58845 96B/80B sig a8f8f002 (=P120-PB0);
  PB1 58846 100B/84B fat sig 03000000; PBA
  58847..58862 (16, 100B/84B sig 37000000
  =P118-PBA); NO extra singleton; PBB10 58863..
  58872 (10, 100B/84B sig 02000000 =P116-PB1-
  fat, uniform M 10/10); QUAD 58873..58936
  (64=4x16, ALL 100B/84B, SINGLE sig 22000000
  NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,48,49,50,51,76-79] exact (b5 const 0xcb);
  PBB VPOS [4,44,45,46,47,49,50,51,80-83]
  exact (12B).

## 2. quad rows: CONFIRM
- M 6B pos[6,7,76,77,78,79] row-indep 16/16
  x4, full-tuple 16/16 distinct each row
  (heads b6,7 15/16 distinct pairs).
- R-band 7B b44,45,46,47,49,50,51 row-only:
  rows1==3 exact a85b4e2c30fb27; row0
  4867d031308a6f; row2 48bb6e37b0821f.
- Tails b80..83 row-const ALL distinct
  166f91c6/1476e73f/db372189/15f36855.
- M-novelty vs P120M: ALL NEW (0/16 full, 0/16
  tails; 6B vs 5B layout). PBA M 8B 16/16;
  PBB M 11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xcb PBA/PBB10; quad 0xcb->0xcc
  step exactly at 58880.
- Quad varpos fully partitioned (counter+b5+
  R7+M6+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
