# A-154 (Q-148): T10P139 P-head geometry — DERIVED

Bed: census N=65109..65200 own bed (.rav[12:-4]).
First-hand; P138-M re-derived 64789 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 65109 96B/80B sig 20f313a8 NEW; PB1
  65110 100B/84B fat sig af000000 NEW (1st af
  fat); PBA 65111..65126 (16, 100B/84B sig
  99080000 NEW); NO extra singleton; PBB10
  65127..65136 (10, 100B/84B sig ae000000 NEW,
  1st ae); QUAD 65137..65200 (64=4x16, ALL
  100B/84B, SINGLE sig 1a0a0000 NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,32,33,34,38,39,76-79] exact (b5 const
  0xfc); PBB VPOS [4,29,30,31,37,38,39,40,41,
  42,80-83] exact (14B).

## 2. quad rows: CONFIRM + PBA-M CORRECT (3rd 0==3)
- M 7B pos[44,45,46,76,77,78,79] row-indep
  16/16 x4, full-tuple 16/16 distinct each row
  (heads b44,45,46 15/16 distinct triples).
- R-band 8B b32,33,37,38,39,40,41,42 row-only:
  rows0==3 exact 2a53c86e316eeff8; row1
  8a053468694ebaf8; row2 ea0b6865790e0bf9.
- Tails b80..83 row-const db34edb3/77b30359/
  f12e8768/d835edb3 (rows0,3 differ b0 only).
- M-novelty vs P138M: ALL NEW (0/16 full, 0/16
  tails; 7B vs 8B layout). PBA M 9B 16/16 --
  NOT 8B (VPOS-confirmed: 5 heads b32,33,34,
  38,39 + 4 tails); PBB M 13B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xfc PBA/PBB; quad 0xfc->0xfd step
  exactly at 65152.
- Quad varpos fully partitioned (counter+b5+
  R8+M7+tails), 0 stragglers. NO D-class dips.

## legs 1+3 agree; leg2 CORRECTS PBA M 8B->9B
