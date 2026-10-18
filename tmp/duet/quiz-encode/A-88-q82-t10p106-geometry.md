# A-88 (Q-82): T10P106 P-head geometry — DERIVED

Bed: census cells N=53625..53716 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 53625 sig 9d4b4800; PB1 53626 sig 08796b90;
  PBA 53627..53642 (16, 100B/84B sig 09000000); PBB
  single 53643 sig e878ce91 + 53644..53652 (9, sig
  e878ce49, split-sig pair); QUAD 53653..53716 (64=4x16,
  ALL 100B/84B, SINGLE sig 04000000 — migrated from
  P105-PBA).
- PBA VPOS [4,5,20,21,76,77,78,79] EXACT; PBB9 VPOS
  [4,16,17,18,19,20,21,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM
- M 8B pos[18,19,26,27,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b20,22,23,24,25: row0==row1 a2535dede7;
  row2 6e83802dd9; row3 6f83802dd9.
- tails b80..83: 24286b2f/9b286b2f/1bcdd967/a28f3c1c.
- PBA M 6B pos[20,21,76-79] 16/16; PBB9 M 10B
  pos[16-21,76-79] 9/9.

## 3. counters + dips: CONFIRM, NONE
- b4=(0xf3+2off) 92/92 whole tier (PBA carry 53631->
  53632); quad-local b4=(0x2b+2off) 64/64, b5=0xa3 const.
- 12x96B + 80x100B. NO D-class dips.

## geometry agrees on all 3 legs
