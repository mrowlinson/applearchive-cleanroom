# A-128 (Q-122): T10P126 P-head geometry — DERIVED

Bed: census N=60585..60676 own bed (.rav[12:-4]).
First-hand; P125-M re-derived 60265 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 60585 96B/80B sig 2a78cd04 NEW; PB1
  60586 100B/84B fat sig 04000000; PBA 60587..
  60602 (16, 100B/84B sig 43000000 =P125-PBA);
  NO extra singleton; PBB10 60603..60612 (10,
  100B/84B sig 04000000 =PB1 sig, 1st PB1==PBB);
  QUAD 60613..60676 (64=4x16, ALL 100B/84B,
  SINGLE sig 43000000 =own PBA sig, self-PBA
  reuse 2nd).
- 1x96B + 91x100B exact. PBA VPOS
  [4,44,45,46,47,76-79] exact (b5 const 0xd9);
  PBB VPOS [4,11,31,41,42,43,48,49,80-83]
  exact (12B).

## 2. quad rows: CONFIRM (1st 8B M)
- M 8B pos[48,49,50,51,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b48-51 14/16 distinct quads).
- R-band 8B b11,31,41,42,43,44,45,46 row-only,
  ALL 4 distinct: 9dba71e541303562/614a31e5
  3ff0da61/0f9aa1e143709162/614a39e53ff0da61
  (rows1,3 differ 1B).
- Tails b80..83 row-const ALL distinct
  2ca9ac8d/01174800/8f5ff286/ad02a210.
- M-novelty vs P125M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 7B layout). PBA M 8B 16/16;
  PBB M 11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xd9 PBA/PBB; quad 0xd9->0xda step
  exactly at 60672.
- Quad varpos fully partitioned (counter+b5+
  R8+M8+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
