# A-144 (Q-138): T10P134 P-head geometry — DERIVED

Bed: census N=63369..63460 own bed (.rav[12:-4]).
First-hand; P133-M re-derived 63049 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 63369 96B/80B sig 74f25d28 NEW; PB1
  63370 100B/84B fat sig 28000000 NEW (1st 28
  fat); PBA 63371..63386 (16, 100B/84B sig
  a6030000 NEW); SINGLETON 63387 100B/84B sig
  2b000000 NEW; SINGLETON 63388 100B/84B sig
  2d000000 NEW (2nd P115-style double); PBB8
  63389..63396 (8, 100B/84B sig 2e000000 NEW);
  QUAD 63397..63460 (64=4x16, ALL 100B/84B,
  SINGLE sig a6030000 =own PBA sig, self-PBA
  reuse 3rd).
- 1x96B + 91x100B exact. PBA VPOS
  [4,44,45,46,76-79] exact (b5 const 0xef);
  PBB VPOS [4,11,31,41,42,43,48,49,80-83]
  exact (12B).

## 2. quad rows: CONFIRM
- M 8B pos[48,49,50,51,76,77,78,79] (5th 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads b48-51 14/16 distinct quads).
- R-band 9B b33,34,35,41,42,43,44,45,46
  (widest) row-only, ALL 4 distinct: 4b3743
  63e689b0d22c/cb6c4393e601b0d32b/4b5c436b
  e21390562d/cb4c41ebe101d0512c.
- Tails b80..83 row-const ALL distinct
  041423ab/ae1dd1f3/f41d59a2/d4473ffd.
- M-novelty vs P133M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 8B layout). PBA M 7B 16/16;
  PBB M 11B 8/8.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 88 grouped
  cells (16+8+64) + PB0/PB1/singletons (92/92).
- b5 const 0xef PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R9+
  M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
