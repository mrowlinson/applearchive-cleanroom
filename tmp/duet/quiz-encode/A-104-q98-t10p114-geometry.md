# A-104 (Q-98): T10P114 P-head geometry — DERIVED

Bed: census N=56409..56500 own bed (.rav[12:-4]).
First-hand this shift.

## 1. shape: CONFIRM (PBB10 restored)
- PB0 56409 96B sig 02ba9e01 NEW; PB1 56410 100B
  fat 01000000 (6th); PBA 56411..56426 (16, 100B/84B
  sig 19000000 NEW); PBB 56427..56436 (10, 96B/80B
  sig d67947cf NEW, no singleton); QUAD
  56437..56500 (64=4x16, ALL 100B/84B, SINGLE sig
  0c000000 NEW, 6th consecutive).
- PBA VPOS [4,20,21,76-79] EXACT; PBB VPOS
  [4,16-22,76-79] EXACT. 11x96B + 81x100B.

## 2. quad rows: CONFIRM+SPLIT
- Writer 10B band b18..27 splits first-hand:
  M 8B pos[18,19,26,27,76,77,78,79] row-indep
  16/16 x4, 16/16 distinct; R-band b20-25 row-only:
  row0 51db3e5f0e87, row1==row3 725c03face70,
  row2 475dce08ae9d. b5 = counter, not M.
- tails b80..83 row-const d1fb7ff0/617f3fa5/
  dcfdd54b/4d33a6df (all distinct).
- PBA M 6B pos[20,21,76-79] 16/16; PBB M 11B
  pos[16-22,76-79] 10/10.

## 3. counters + dips: DERIVED, NONE
- tier b4=(0xb3+2off) 92/92, b5=0xb8+(n>=56448)
  92/92 (step inside quad @off11 255/184->1/185);
  pay[4:6]==LE((n<<1)|1)&FFFF 92/92.
- quad b4=(0xeb+2off) 64/64. NO D-class dips.

## geometry agrees on all 3 legs
