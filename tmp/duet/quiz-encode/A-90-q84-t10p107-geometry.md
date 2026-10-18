# A-90 (Q-84): T10P107 P-head geometry — DERIVED

Bed: census cells N=53973..54064 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 53973 sig 9d849000; PB1 53974 sig e878ce91
  (= P106-PBB-single sig, migrant, first-hand); PBA
  53975..53990 (16, 100B/84B sig 09000000, same as
  P106-PBA); PBB 53991..54000 (10, SINGLE sig e878ce4f
  NEW, no single); QUAD 54001..54064 (64=4x16, ALL
  100B/84B, SINGLE sig 04000000, same as P106-quad).
- PBA VPOS [4,38,39,76,77,78,79] EXACT; PBB VPOS
  [4,25,26,27,33,34,35,36,37,38,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (3+1)
- M 7B pos[44,45,46,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b29,30,31,38,39,40,41: row0==row1==row2
  04b7831b178cd9; row3 unique 44fb82b9f76cd3.
- tails b80..83: f3e5e967/69e6e967/145c4a74/d19aa1ac.
- PBA M 6B pos[38,39,76-79] 16/16; PBB M 13B
  pos[25-27,33-38,76-79] 10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0xab+2off) 92/92 whole tier; quad qb4=(0xe3+2off)
  64/64, carry AT row edge 54015->54016 (b5 {165,166}).
- 12x96B + 80x100B. NO D-class dips.

## geometry agrees on all 3 legs
