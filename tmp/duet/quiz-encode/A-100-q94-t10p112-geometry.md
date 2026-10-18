# A-100 (Q-94): T10P112 P-head geometry — DERIVED

Bed: census cells N=55713..55804 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 55713 96B sig 42887701 (same sig as P111-PB0);
  PB1 55714 100B fat sig 01000000 (4th same-sig fat
  PB1); PBA 55715..55730 (16, 100B/84B sig 17000000);
  PBB 55731..55740 (10, SINGLE sig 0e7851bb NEW, back
  to single-sig); QUAD 55741..55804 (64=4x16, ALL
  100B/84B, SINGLE sig 0b000000, 4th consecutive).
- PBA VPOS [4,32,33,34,76,77,78,79] EXACT; PBB VPOS
  [4,28,29,30,31,32,33,34,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (1st row-arithmetic M byte)
- M 7B pos[30,31,39,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- b38 = X(m) + rowoff(r), rowoff=(0,0,+1,-1): 16/16
  cols first-hand (rows0,1 share; row2 +1; row3 -1).
- row-bytes b32-37: row0==row1 fcfc7fc9505d; row2
  dbfc1b459022; row3 17bfcf0d70fd (2+1+1).
- tails b80..83: e2f64f85/52f74f85/7ab50470/37b7fada.
- PBA M 7B pos[32,33,34,76-79] 16/16; PBB M 11B
  pos[28-34,76-79] 10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0x43+2off) 92/92 whole tier; quad qb4=(0x7b+2off)
  64/64 no wrap, b5=0xb3 const 64/64.
- 11x96B + 81x100B. NO D-class dips.

## geometry agrees on all 3 legs
