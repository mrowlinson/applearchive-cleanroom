# A-76 (Q-70): T10P100 P-head geometry — DERIVED

Bed: census cells N=51537..51628 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 51537 sig 19df0300; PB1 51538 sig 6ebcc307; PBA
  51539..51554 (16, sig e0c63b7c); single 51555 (sig
  a619df04); PBB 51556..51564 (9, SINGLE sig d38c6f02);
  QUAD 51565..51628 (64=4x16, SINGLE sig 37cdf826 all
  4 rows). All 96B/80B.
- PBB10 VPOS [0,1,2,3,4,6,7,8,9,10,11,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM
- M 6B pos[13,14,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- row0/row1 rb differ ONLY b6 (cd/cf, rest 5fbac98ee8);
  row2 == row1 rb; row3 unique b75bda3fc1e6
  (pos[6,7,8,9,10,11]).
- tails fde69467/818c0f42/018d0f42/534edea2; rows1,2
  share last2B 0f42. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0xa3+2off) 92/92 (b5 set
  {146,147}); quad-local (0xdb+2off) 64/64; wrap
  row1m2->m3 51583 255/146 -> 51584 1/147;
  b5=0x92+(off>=19) 64/64.
- PBA VPOS [4,6,7,8,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
