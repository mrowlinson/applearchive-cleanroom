# A-82 (Q-76): T10P103 P-head geometry — DERIVED

Bed: census cells N=52581..52672 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 52581 sig fca20900; PB1 52582 sig e4fca209
  (PB0-sig-led); PBA 52583..52598 (16, sig 5ace2f9a).
  All 96B/80B.
- PBB 52599..52608 SIG-VARIEGATED in EXACT writer order:
  3278ee09/dc78ca05/e6783004/dc78ca05/ea783004/
  ea783004/4679e004/7e792505/4679e004/4679e004.
  PBB VPOS [0-5,12-19,76-79] EXACT.
- QUAD 52609..52672 ROW-SIGS: row0=row2 4679e04c,
  row1 ec78304c, row3 8a79254d (each single).

## 2. quad rows: CONFIRM
- M 6B pos[16,17,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- row0==row2 sig + rb 9584ec; row1 unique d5edfa;
  row3 unique 9556de (pos[12,13,14]).
- tails 3bf2da6a/b4f6c703/32f3da6a/74b1e8f5; rows0,2
  share last2B da6a. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0xcb+2off) 92/92 (b5 set
  {154,155}); quad-local (0x03+2off) 64/64, max 0x81,
  NO wrap; b5=0x9b const 64/64.
- PBA VPOS [4,13,14,15,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
