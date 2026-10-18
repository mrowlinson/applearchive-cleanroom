# A-94 (Q-88): T10P109 P-head geometry — DERIVED

Bed: census cells N=54669..54760 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM (1st fat PB1)
- PB0 54669 96B sig 9dc4b000; PB1 54670 100B sig
  01000000 (1st fat PB1, first-hand); PBA 54671..54686
  (16, 100B/84B sig 17000000); PBB 54687..54696 (10,
  SINGLE sig 26f8ceb0 NEW, no single); QUAD
  54697..54760 (64=4x16, ALL 100B/84B, SINGLE sig
  0b000000 all rows).
- PBA VPOS [4,11,18,19,26,27,76,77,78,79] EXACT; PBB
  VPOS [4,14,15,21,22,23,24,25,26,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (1st alternating)
- M 6B pos[32,33,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b18,19,25,26,27,28,29: row0==row2
  219790c42fd063; row1==row3 01d280cd7f100f
  (alternating, first-hand).
- tails b80..83: 0f560e69/0dede575/fd5f0f69/5e5df375.
- PBA M 9B pos[11,18,19,26,27,76-79] 16/16; PBB M 12B
  pos[14,15,21-26,76-79] 10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0x1b+2off) 92/92 whole tier; quad qb4=(0x53+2off)
  64/64 no wrap, b5=0xab const 64/64.
- 11x96B + 81x100B. NO D-class dips.

## geometry agrees on all 3 legs
