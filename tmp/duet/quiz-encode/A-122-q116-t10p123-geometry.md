# A-122 (Q-116): T10P123 P-head geometry — DERIVED

Bed: census N=59541..59632 own bed (.rav[12:-4]).
First-hand; P122-M re-derived 59221 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 59541 96B/80B sig f6782402 NEW; PB1
  59542 100B/84B fat sig 07000000 NEW (1st 07
  fat); PBA 59543..59558 (16, 100B/84B sig
  79000000 NEW); NO extra singleton; PBB10
  59559..59568 (10, 100B/84B sig 01000000);
  QUAD 59569..59632 (64=4x16, ALL 100B/84B,
  SINGLE sig 1e000000 =P122-quad-sig).
- 1x96B + 91x100B exact. PBA VPOS
  [4,29,38,39,76-79] exact (b5 const 0xd1);
  PBB VPOS [4,29,30,31,37,38,39,40,41,42,
  80-83] exact (14B).

## 2. quad rows: CONFIRM
- M 7B pos[44,45,46,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b44,45,46 14/16 distinct triples; b46
  2 values b0/b1 only).
- R-band 8B b29,30,31,37,38,39,40,41 row-only,
  ALL 4 distinct: 29cff32ff2f64d46/a975f3ef
  2017cd38/a98bf7ef75970d54/a975f36f2617cd38
  (rows1,3 differ mid-bytes).
- Tails b80..83 row-const ALL distinct
  2c9aef49/eb265226/b1629c3e/0d9be82e.
- M-novelty vs P122M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 7B layout). PBA M 7B 16/16;
  PBB M 13B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xd1 PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R8+
  M7+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
