# A-152 (Q-146): T10P138 P-head geometry — DERIVED

Bed: census N=64761..64852 own bed (.rav[12:-4]).
First-hand; P137-M re-derived 64441 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 64761 96B/80B sig 14f352aa NEW; PB1
  64762 100B/84B fat sig aa000000 NEW (1st aa
  fat); PBA 64763..64778 (16, 100B/84B sig
  a60a0000 NEW); NO extra singleton; PBB10
  64779..64788 (10, 100B/84B sig aa000000 =PB1
  sig, PB1==PBB 3rd); QUAD 64789..64852
  (64=4x16, ALL 100B/84B, SINGLE sig fe0a0000
  NEW).
- 1x96B + 91x100B exact. PBA VPOS
  [4,5,20,76-79] exact (b5 0xf9->0xfa @64768,
  3rd intra-PBA step); PBB VPOS [4,20,21,22,
  23,24,25,26,80-83] exact (12B).

## 2. quad rows: CONFIRM + tails CORRECT (4th xor-byte)
- M 8B pos[11,18,19,27,76,77,78,79] (8th 8B M)
  row-indep 16/16 x4, full-tuple 16/16 distinct
  each row (heads 12/16 distinct quads).
- b26 xor-row: rows0,1,3 = M26[m] pat
  f55595d5..., row2 = ^0x03 16/16, 64/64 exact.
- R-band 6B b20,21,22,23,24,25 row-only:
  rows0==3 exact 78de44e10fcb (2nd 0==3); row1
  91dd26e2cf4a; row2 685ebf458f0d.
- Tails d970c482/8e3aec0e/5e386d3d/652dc5a0
  exact values -- BUT rows0,3 differ 4B, NOT 2B
  (d9/65, 70/2d, c4/c5, 82/a0 all differ).
- M-novelty vs P137M: ALL NEW (0/16 full, 0/16
  tails; 8B vs 8B layout). PBA M 5B 16/16
  (smallest PBA M); PBB M 11B 10/10.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 0xf9->0xfa step @64768 (PBA), const 0xfa
  PBB/quad.
- Quad varpos fully partitioned (counter+R6+
  xor+M8+tails), 0 stragglers. NO D-class dips.

## legs 1+3 agree; leg2 CORRECTS tails 0v3 2B->4B
