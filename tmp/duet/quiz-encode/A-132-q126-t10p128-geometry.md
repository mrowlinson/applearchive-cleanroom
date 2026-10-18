# A-132 (Q-126): T10P128 P-head geometry — DERIVED

Bed: census N=61281..61372 own bed (.rav[12:-4]).
First-hand; P127-M re-derived 60961 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 61281 96B/80B sig ccf18e08 NEW; PB1
  61282 100B/84B fat sig 10000000 NEW (1st 10
  fat); PBA 61283..61298 (16, 100B/84B sig
  0d010000 NEW); NO extra singleton; PBB10
  61299..61308 (10, 100B/84B sig 08000000 NEW,
  1st 08); QUAD 61309..61372 (64=4x16, ALL
  100B/84B, SINGLE sig 86000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,32,33,34,76-79] exact (b5 const 0xde);
  PBB VPOS [4,32,33,34,35,36,37,38,80-83]
  exact (12B).

## 2. quad rows: CONFIRM (2nd xor-byte)
- M 7B pos[29,30,39,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b29,30,39 15/16 distinct triples).
- b38 row-xor: rows = M38[m]^XROW[q], XROW
  00/07/01/07 (rows1==3), 64/64 exact.
- R-band 5B b32,34,35,36,37 row-only:
  rows1==3 exact 420f425189; row0 ac27fdf156;
  row2 2393123129. b33 const 0xbf in quad.
- Tails b80..83 row-const ALL distinct
  01745910/ba74eb37/5cef5328/e876eb37.
- M-novelty vs P127M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 8B layout). PBA M 7B 16/16;
  PBB M 11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xde PBA/PBB; quad 0xde->0xdf step
  exactly at 61312.
- Quad varpos fully partitioned (counter+b5+
  R5+xor+M7+tails), 0 stragglers. NO D-class
  dips.

## geometry agrees on all 3 legs
