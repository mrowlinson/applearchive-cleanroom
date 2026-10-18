# A-92 (Q-86): T10P108 P-head geometry — DERIVED

Bed: census cells N=54321..54412 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 54321 sig 9dc49000; PB1 54322 sig e878cee9; PBA
  54323..54338 (16, 100B/84B sig 0e000000); PBB
  54339..54348 (10, SINGLE sig 854e6258 NEW, no single);
  QUAD 54349..54412 (64=4x16, ALL 100B/84B, SINGLE sig
  05000000 all rows).
- PBA VPOS [4,6,7,12,76,77,78,79] EXACT; PBB VPOS
  [4,6,7,8,9,10,11,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (1B-apart pair)
- M 7B pos[9,10,11,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b6,7,12,13,14: row0 c25d0f7c3d vs row1
  c35d0f7c3d (1B apart, first-hand); row2 5b59dd1454;
  row3 05dc114427. All 4 distinct.
- tails b80..83: 4a2abcf6/560d49bc/c551a3bd/f49cc76e.
- PBA M 7B pos[6,7,12,76-79] SAME layout as P105M,
  0/16 overlap first-hand. PBB M 10B pos[6-11,76-79]
  10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0x63+2off) 92/92 whole tier; quad qb4=(0x9b+2off)
  64/64, carry mid-row3 54399->54400 (b5 {168,169}).
- 12x96B + 80x100B. NO D-class dips.

## geometry agrees on all 3 legs
