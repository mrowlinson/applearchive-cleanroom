# A-156 (Q-150): T10P140 P-head geometry — DERIVED

Bed: census N=65457..65548 own bed (.rav[12:-4]).
First-hand; P139-M re-derived 65137..65152 row0
(this seat).

## 1. shape: CONFIRM + CORRECT PBB sig list
- PB0 65457 96B/80B sig 20f313a8 (=P139-PB0);
  PB1 65458 100B/84B fat sig fb000000 NEW;
  PBA 65459..65474 (16, 100B/84B sig bf0f0000
  NEW); SINGLETON 65475 100B/84B sig b9000000
  NEW; PBB 65476..65484 (9, 100B/84B MIXED
  b8/5d — 1st mixed-sig PBB CONFIRMED).
- CORRECT: writer lists 10 sig tokens for 9 PBB
  cells (extra leading b8). Own per-N first-hand:
  65476..65484 = b8,5d,5d,5d,b8,5d,b8,5d,b8
  (== writer tokens 2..10 exactly; drop token 1).
- QUAD 65485..65548 (64=4x16, ALL 100B/84B):
  rows0,1 sig cb050000 NEW; row2 sig 940b0000
  NEW; row3 SPLIT cols0-2 cb050000 / cols3-15
  970b0000 NEW (flip col3 = N 65536 = 2^16).
- 1x96B + 91x100B exact. PBA VPOS [4,6,7,76-
  79] exact (b5 const 0xff); PBB VPOS [0,4,6,
  7,8,9,10,11,80-83] exact (12B).

## 2. quad rows: CONFIRM
- M 7B pos[13,14,15,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct each row (heads
  15/16 distinct triples each row).
- R-band 7B b6,7,8,9,10,11,49 5-state exact:
  r0 035f3c2808fd08 / r1 585ddc1702e508 /
  r2 425a1dcb7b0908 / r3a  ab5bdc71e0f008 /
  r3b 56b79de3c0e148, 64/64 (1st split-row).
- Sig 5-state cb05/cb05/940b/cb05/970b same
  split. Tails b80..83 row-const UNSPLIT
  6eae3f7e/47bb09b8/a87297a7/1b7387e8.
- M-novelty vs P139M: ALL NEW (16/16 full +
  16/16 heads + 16/16 tails). PBA M 6B 16/16;
  PBB M 11B 9/9.

## 3. counters + dips: CONFIRM, NONE
- pay[4:6]==LE((n<<1)|1)&FFFF all 90 grouped
  cells (also PB0/PB1: 63ff/65ff exact).
- b5 const 0xff PBA/SING/PBB/rows0-2+3a,
  0x00 row3b (2^16 step @65536).
- Quad varpos fully partitioned (counter+sig2+
  R7+M7+tails = 22 var, 62 const), 0
  stragglers. NO D-class dips.

## legs 2-3 agree; leg1 CORRECTS PBB sig list
