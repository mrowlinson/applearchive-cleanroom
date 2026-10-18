# A-72 (Q-66): T10P98 P-head geometry — DERIVED

Bed: census cells N=50841..50932 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 50841 sig c6810300; PB1 50842 sig 6a7c9803; PBA
  50843..50858 (16, sig 6a7c9838); PBB 50859..50868 (10,
  SINGLE sig 6ebcc301); QUAD 50869..50932 (64=4x16,
  SINGLE sig 6ebcc31c all 4 rows). All 96B/80B.

## 2. quad rows: CONFIRM (3+1)
- M 8B pos[24,25,26,27,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- rows0-2 share rb 6e946ac4f68dd6; row3 unique
  ee13aa1fd72dcd (pos[12,13,17,18,19,20,21]).
- tails f00e3d10/30dba410/b3dba410/86d5f802; rows1,2
  share last3B dba410. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x33+2off) 92/92; quad-local
  (0x6b+2off) 64/64, max 0xe9, NO wrap; b5=0x8d const
  64/64 (whole-tier set {141}).
- PBA VPOS [4,16,17,18,72,73,74,75] EXACT; PBB VPOS
  [4,12,13,14,17,18,19,20,21,22,76,77,78,79] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
