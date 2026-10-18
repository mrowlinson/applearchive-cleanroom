# A-96 (Q-90): T10P110 P-head geometry — DERIVED

Bed: census cells N=55017..55108 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM (variegated PBB)
- PB0 55017 96B sig 42886101; PB1 55018 100B fat sig
  01000000 (same sig as P109-PB1, first-hand); PBA
  55019..55034 (16, 100B/84B sig 16000000); PBB
  55035..55044 (10, VARIEGATED 26f8ce + b8/96/80/fa/b2/
  da/fa/da/fa/fa, first-hand set); QUAD 55045..55108
  (64=4x16, ALL 100B/84B, SINGLE sig 0b000000, same as
  P109-quad).
- PBA VPOS [4,44,45,46,76,77,78,79] EXACT; PBB10 VPOS
  [3,4,5,27,37,38,39,44,45,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (3+1)
- M 6B pos[50,51,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b11,31,41,42,43,48,49: row0==row1==row2
  5afb92f21fd216; row3 unique 7adb72f0118215.
- tails b80..83: 60720d51/d2720d51/44730d51/42f8690f
  (rows0-2 share x720d51/x730d51).
- PBA M 7B pos[44,45,46,76-79] SAME layout as P107M,
  0/16 overlap first-hand. PBB M 12B pos[3,27,37,38,39,
  44,45,76-79] (incl. sig byte) 10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0xd3+2off) 92/92 whole tier (PBB carry 55039->
  55040); quad qb4=(0x0b+2off) 64/64, b5=0xae const.
- 11x96B + 81x100B. NO D-class dips.

## geometry agrees on all 3 legs
