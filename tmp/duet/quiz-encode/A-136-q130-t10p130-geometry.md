# A-136 (Q-130): T10P130 P-head geometry — DERIVED

Bed: census N=61977..62068 own bed (.rav[12:-4]).
First-hand; P129-M re-derived 61657 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 61977 96B/80B sig ccf18e08 (3rd); PB1
  61978 100B/84B fat sig 13000000 NEW (1st 13
  fat); PBA 61979..61994 (16, 100B/84B sig
  34010000 NEW); NO extra singleton; PBB10
  61995..62004 (10, 100B/84B sig 09000000
  =P127-PB1-fat); QUAD 62005..62068 (64=4x16,
  ALL 100B/84B, SINGLE sig 92000000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,20,21,22,76-79] exact (b5 const 0xe4);
  PBB VPOS [4,20,21,22,23,24,25,26,80-83]
  exact (12B).

## 2. quad rows: CONFIRM (3rd xor-byte)
- M 6B pos[18,27,76,77,78,79] row-indep 16/16
  x4, full-tuple 16/16 distinct each row
  (heads b18,27 10/16 distinct pairs).
- b26 xor-row: rows0,1,3 = M26[m] pat
  f0f060f0..., row2 = ^0x01 16/16, 64/64 exact.
- R-band 6B b20,21,22,23,24,25 row-only, ALL 4
  distinct: 6cdb14754fe7/98dd03ec2f8b/685e54
  d6cf16/625d832ecfb8.
- Tails b80..83 row-const ALL distinct
  91afc594/7330419f/52f42a07/21fd3088.
- M-novelty vs P129M: ALL NEW (0/16 full, 0/16
  tails; 6B vs 6B layout). PBA M 7B 16/16;
  PBB M 11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xe4 PBA/PBB/quad (no step).
- Quad varpos fully partitioned (counter+R6+
  xor+M6+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
