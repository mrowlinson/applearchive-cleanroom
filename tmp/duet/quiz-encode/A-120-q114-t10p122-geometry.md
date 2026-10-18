# A-120 (Q-114): T10P122 P-head geometry — DERIVED

Bed: census N=59193..59284 own bed (.rav[12:-4]).
First-hand; P121-M re-derived 58873 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 59193 96B/80B sig a8f8f002 (3rd); PB1
  59194 100B/84B fat sig 03000000; PBA 59195..
  59210 (16, 100B/84B sig 3a000000 NEW);
  SINGLETON 59211 100B/84B sig 03000000 (=PB1);
  PBB 59212..59220 (9, 100B/84B sig 01000000,
  4th 100B PBB); QUAD 59221..59284 (64=4x16,
  ALL 100B/84B, SINGLE sig 1e000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,20,21,22,76-79] exact (b5 const 0xce);
  PBB VPOS [4,20,21,22,23,24,25,26,80-83]
  exact (12B).

## 2. quad rows: CONFIRM
- M 7B pos[18,26,27,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b18,26,27 14/16 distinct triples).
- R-band 6B b20,21,22,23,24,25 row-only:
  rows1==3 exact a2ddea43aeb4; row0
  4bdc037c2ed5; row2 1ade40f54ef6.
- Tails b80..83 row-const ALL distinct
  1b7a6717/c3761180/d6716f5c/8d2f1280.
- M-novelty vs P121M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 6B layout). PBA M 7B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xce PBA/PBB; quad 0xce->0xcf step
  exactly at 59264.
- Quad varpos fully partitioned (counter+b5+
  R6+M7+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
