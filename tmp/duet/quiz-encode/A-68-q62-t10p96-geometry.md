# A-68 (Q-62): T10P96 P-head geometry — DERIVED

Bed: census cells N=50145..50236 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.
(ACK PARENT-043: 2nd poll miss — now auditing Q-* vs
A-*/MOOT-* explicitly every turn; gap closed.)

## 1. shape: CONFIRM
- PB0 50145 sig ad550300; PB1 50146 sig e33c7403; PBA
  50147..50162 (16, sig e33c7435); PBB 50163..50172 (10,
  SINGLE sig e33c7401); QUAD 50173..50236 (64=4x16,
  SINGLE sig e33c741b all 4 rows). All 96B/80B. All
  head sigs same e33c74 family.

## 2. quad rows: CONFIRM
- M 6B pos[34,35,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct.
- row0/row1 differ ONLY b28 (1e/23, rest f34e8f53);
  row2/row3 differ ONLY b28 (87/89, rest 7bc40f2b).
- tails all distinct: 9f7c4612/d7793d13/4f33dc68/
  f933f735. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0xc3+2off) 92/92; quad-local
  (0xfb+2off) 64/64; wrap row0m2->m3 50175 255/135 ->
  50176 1/136; b5=0x87+(off>=3) 64/64 (set {135,136}).
- PBA VPOS [4,28,72,73,74,75]; PBB VPOS
  [4,24,25,29,30,31,32,33,34,76,77,78,79] — both EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
