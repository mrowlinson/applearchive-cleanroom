# A-112 (Q-106): T10P118 P-head geometry — DERIVED

Bed: census N=57801..57892 own bed (.rav[12:-4]).
First-hand; P117-M re-derived 57481 row0 +
P117-PBA sig re-derived 57455 (this seat).

## 1. shape: CONFIRM
- PB0 57801 96B/80B sig f03ab501; PB1 57802
  100B/84B fat sig 03000000 (1st 03 fat);
  PBA 57803..57818 (16, 100B/84B sig
  37000000); SINGLETON 57819 100B/84B sig
  03000000 (=PB1); PBB 57820..57828 (9,
  100B/84B sig 01000000 -- 1st 100B PBB);
  QUAD 57829..57892 (64=4x16, ALL 100B/84B,
  SINGLE sig 1b000000).
- 1x96B + 91x100B exact. PBA VPOS
  [4,44,45,46,76-79] exact; PBB VPOS
  [4,11,31,41,42,43,48,49,80-83] exact
  (12B incl b80-83).
- Quad sig =P117-PBA-sig first-hand (57455
  derived 100B sig 1b000000). 1st quad
  reuse of a PBA sig stands.

## 2. quad rows: CONFIRM + linkage ANSWERED
- M 7B pos[44,50,51,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row.
- R-band 7B b11,31,41,42,43,48,49 row-only
  (1 distinct/row): rows0,1,3 42a078e4a5864c,
  row2 a0e0b8e6317d4e exact.
- Tails b80..83 row-const 421c8f19/31d58f19/
  87c82927/1388a41a exact.
- Linkage YES: both quad R values occur as
  PBB R-parts (42a078e4a5864c @57823,57827;
  a0e0b8e6317d4e @57826,57828) -- prefixes
  of PBB-M rows. (Near-twin a0e0b0e6317d4e
  @57821 differs b1 b8->b0.)
- M-novelty vs P117M: ALL NEW (0/16 overlap;
  P117M 16 distinct own bed, heads b32,33,34
  vs b44,50,51). PBA M 7B 16/16; PBB M 12B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 89 grouped
  cells, 0 bad; PB0/PB1/singleton match too
  (92/92).
- b5 const 0xc3 PBA/PBB; quad single step
  0xc3->0xc4 at 57856 (inside row1).
- varpos fully partitioned (counter+R+M+tails
  per group), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
