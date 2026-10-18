# A-70 (Q-64): T10P97 P-head geometry — DERIVED

Bed: census cells N=50493..50584 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 50493 sig c6510300; PB1 50494 sig e33c7403; PBA
  50495..50510 (16, sig e33c7436); single 50511 (sig
  e33c7402); PBB 50512..50520 (9, SINGLE sig e33c7401);
  QUAD 50521..50584 (64=4x16, SINGLE sig 30ce4317 all
  4 rows). All 96B/80B.
- PBB10 VPOS [3,4,15,27,37,38,39,46,47,76,77,78,79]
  EXACT; split-sig b3 02 (50511) / 01 (PBB9).

## 2. quad rows: CONFIRM (1+3)
- M 6B pos[6,7,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW (0/16 vs P96-M, 0/16 vs R94-M).
- row0 rb unique 9274e7bb5377; rows1-3 IDENTICAL rb
  86c41f924176 (pos[27,37,38,39,46,47]).
- tails 44cc4ea0/26094598/6e884698/f3884698; rows1-3
  share last2B 4698. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x7b+2off) 92/92; quad-local
  (0xb3+2off) 64/64; wrap row2m6->m7 50559 255/138 ->
  50560 1/139; b5=0x8a+(off>=39) 64/64 (set {138,139}).
- PBA VPOS [4,40,41,46,47,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
