# A-140 (Q-134): T10P132 P-head geometry — DERIVED

Bed: census N=62673..62764 own bed (.rav[12:-4]).
First-hand; P131-M re-derived 62353 row0 (this
seat).

## 1. shape: CONFIRM (all-NEW sigs)
- PB0 62673 96B/80B sig e0f3c012 NEW; PB1
  62674 100B/84B fat sig 18000000 NEW (1st 18
  fat); PBA 62675..62690 (16, 100B/84B sig
  83010000 NEW); SINGLETON 62691 100B/84B sig
  16000000 NEW; PBB9 62692..62700 (9, 100B/84B
  sig 0b000000 NEW, 1st 0b, 7th 100B PBB);
  QUAD 62701..62764 (64=4x16, ALL 100B/84B,
  SINGLE sig ab000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,6,7,8,76-79] exact (b5 const 0xe9); PBB
  VPOS [4,6,7,12,13,14,15,80-83] exact (11B).

## 2. quad rows: CONFIRM
- M 7B pos[13,14,15,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b13,14,15 15/16 distinct triples).
- R-band 6B b6,7,8,9,10,11 row-only, ALL 4
  distinct: e5d83cf2a319/19599c206308/bb589c
  ab8e22/30db7c3aeb10.
- Tails b80..83 row-const ALL distinct
  309cbc8c/eae6f8e3/0ad7711f/f58e7e28.
- M-novelty vs P131M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 8B layout). PBA M 7B 16/16;
  PBB M 10B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xe9 PBA/PBB; quad 0xe9->0xea step
  exactly at 62720.
- Quad varpos fully partitioned (counter+b5+
  R6+M7+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
