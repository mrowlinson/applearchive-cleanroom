# A-126 (Q-120): T10P125 P-head geometry — DERIVED

Bed: census N=60237..60328 own bed (.rav[12:-4]).
First-hand; P124-M re-derived 59917 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 60237 96B/80B sig f6782404 (vs f6782402
  P123/124); PB1 60238 100B/84B fat sig
  05000000 (=P124-PB1); PBA 60239..60254 (16,
  100B/84B sig 43000000 NEW); NO extra
  singleton; PBB10 60255..60264 (10, 100B/84B
  sig 04000000); QUAD 60265..60328 (64=4x16,
  ALL 100B/84B, SINGLE sig 43000000 =OWN PBA
  sig, 1st self-PBA reuse).
- 1x96B + 91x100B exact. PBA VPOS
  [4,18,19,26,27,76-79] exact (b5 const 0xd6);
  PBB VPOS [4,18,19,25,26,27,28,29,30,80-83]
  exact (13B).

## 2. quad rows: CONFIRM
- M 7B pos[32,33,34,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b32,33,34 14/16 distinct triples).
- R-band 8B b18,19,25,26,27,28,29,30 row-only:
  rows1==3 exact aacb28c207913245; row0
  2ac698c17331e945; row2 8a1638c64fb1a346.
- Tails b80..83 row-const ALL distinct
  0f102145/0461d3d7/1891af75/e1d27cd8.
- M-novelty vs P124M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 7B layout). PBA M 8B 16/16;
  PBB M 12B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xd6 PBA/PBB; quad 0xd6->0xd7 step
  exactly at 60288.
- Quad varpos fully partitioned (counter+b5+
  R8+M7+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
