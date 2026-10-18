# A-146 (Q-140): T10P135 P-head geometry — DERIVED

Bed: census N=63717..63808 own bed (.rav[12:-4]).
First-hand; P134-M re-derived 63397 row0 (this
seat).

## 1. shape: CONFIRM
- PB0 63717 96B/80B sig 74f25d50 NEW; PB1
  63718 100B/84B fat sig 52000000 NEW (1st 52
  fat); PBA 63719..63734 (16, 100B/84B sig
  3a050000 NEW); SINGLETON 63735 100B/84B sig
  a7000000 NEW; PBB9 63736..63744 (9, 100B/84B
  sig 53000000 NEW, 8th 100B PBB); QUAD 63745..
  63808 (64=4x16, ALL 100B/84B, SINGLE sig
  3b050000 NEW) -- ALL sigs NEW this tier.
- 1x96B + 91x100B exact. PBA VPOS
  [4,13,14,76-79] exact (b5 const 0xf1); PBB
  VPOS [4,5,13,14,15,16,17,18,19,80-83] exact
  (12B, b5 steps 0xf1->0xf2 @63744, 1st
  intra-PBB step).

## 2. quad rows: CONFIRM (1st 0==2 pairing)
- M 6B pos[20,21,76,77,78,79] row-indep 16/16
  x4, full-tuple 16/16 distinct each row
  (heads b20,21 14/16 distinct pairs).
- R-band 6B b13,14,15,16,17,18 row-only:
  rows0==2 exact 5cbc3477fcee; row1
  98bcf1170d6b; row3 243c88d747ac.
- Tails b80..83 row-const bd026f98/ca98057d/
  6d036f98/1d951804 (rows0,2 differ b0 only).
- M-novelty vs P134M: ALL NEW (0/16 full, 0/16
  tails; 6B vs 8B layout). PBA M 6B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells + PB0/PB1 (92/92).
- b5 const 0xf1 PBA; 0xf1->0xf2 step @63744
  (PBB); const 0xf2 quad.
- Quad varpos fully partitioned (counter+R6+
  M6+tails), 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
