# A-130 (Q-124): T10P127 P-head geometry — DERIVED

Bed: census N=60933..61024 own bed (.rav[12:-4]).
First-hand; P126-M re-derived 60613 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 60933 96B/80B sig 2a78cd04 (=P126-PB0);
  PB1 60934 100B/84B fat sig 09000000 NEW (1st
  09 fat); PBA 60935..60950 (16, 100B/84B sig
  99000000 NEW); NO extra singleton; PBB10
  60951..60960 (10, 100B/84B sig 09000000 =PB1
  sig, PB1==PBB 2nd); QUAD 60961..61024
  (64=4x16, ALL 100B/84B, SINGLE sig 9a000000
  NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,13,14,15,76-79] exact (b5 const 0xdc);
  PBB VPOS [4,8,9,10,11,15,16,17,18,19,80-83]
  exact (14B).

## 2. quad rows: CONFIRM
- M 8B pos[20,21,22,23,76,77,78,79] (2nd 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b20-23 15/16 distinct quads).
- R-band 6B b13,14,15,16,17,18 row-only, ALL 4
  distinct: a8fcd577d985/e2bcf3371c57/fefc66
  7790b5/e3bcf3371c57 (rows1,3 differ 1B).
- Tails b80..83 row-const ALL distinct
  940b2818/670e8883/181cde0a/34d01444.
- M-novelty vs P126M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 8B layout). PBA M 7B 16/16;
  PBB M 13B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xdc PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R6+
  M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
