# A-142 (Q-136): T10P133 P-head geometry — DERIVED

Bed: census N=63021..63112 own bed (.rav[12:-4]).
First-hand; P132-M re-derived 62701 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 63021 96B/80B sig e0f3c016 NEW; PB1
  63022 100B/84B fat sig 2a000000 NEW (1st 2a
  fat); PBA 63023..63038 (16, 100B/84B sig
  8a020000 NEW); NO extra singleton; PBB10
  63039..63048 (10, 100B/84B sig 14000000 NEW,
  1st 14); QUAD 63049..63112 (64=4x16, ALL
  100B/84B, SINGLE sig 47010000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,18,19,26,27,76-79] exact (b5 const 0xec);
  PBB VPOS [4,18,19,25,26,27,28,29,30,80-83]
  exact (13B).

## 2. quad rows: CONFIRM
- M 8B pos[32,33,34,35,76,77,78,79] (4th 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b32-35 15/16 distinct quads).
- R-band 8B b18,19,25,26,27,28,29,30 row-only,
  ALL 4 distinct: 0f0bbcc23731b79b/efc60cc6
  3b11b399/af61fccc83f1c19c/cfff4cc10f31b29a.
- Tails b80..83 row-const ALL distinct
  9eab4aad/25289555/25e3439a/c74c1616.
- M-novelty vs P132M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 7B layout). PBA M 8B 16/16;
  PBB M 12B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xec PBA/PBB; quad 0xec->0xed step
  exactly at 63104.
- Quad varpos fully partitioned (counter+b5+
  R8+M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
