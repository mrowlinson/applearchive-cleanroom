# A-98 (Q-92): T10P111 P-head geometry — DERIVED

Bed: census cells N=55365..55456 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM (full-variegated PBB, paired quad)
- PB0 55365 96B sig 42887701; PB1 55366 100B fat sig
  01000000 (3rd same-sig fat PB1); PBA 55367..55382 (16,
  100B/84B sig 17000000, same as P109-PBA); PBB
  55383..55392 (10, FULL-VARIEGATED all-4-byte sigs,
  first-hand set of 8 distinct); QUAD 55393..55456
  (64=4x16, ALL 100B/84B, SINGLE sig 0b000000, 3rd
  consecutive).
- PBA VPOS [4,9,10,11,76,77,78,79] EXACT; PBB10 VPOS
  [0,1,2,3,4,12,13,14,15,76,77,78,79] EXACT.

## 2. quad rows: CONFIRM (2+1+1, 1st paired)
- M 7B pos[20,21,22,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct.
- row-bytes b8,9,10,11,15,16,17,18 (8B): row0==row1
  34f9c2bce0d6dfb0; row2 f4f8ebbda05606c7; row3
  14782fbdc0361c9b (paired, first-hand).
- tails b80..83: 79bd2844/3fef2844/49340d11/48ef2049
  (rows0,1 share 2844).
- PBA M 7B pos[9,10,11,76-79] SAME layout as P108M,
  0/16 overlap first-hand. PBB M 12B pos[0-3,12-15,
  76-79] (incl. full sig) 10/10.

## 3. counters + dips: CONFIRM, NONE
- b4=(0x8b+2off) 92/92 whole tier; quad qb4=(0xc3+2off)
  64/64, carry mid-row1 55423->55424 (b5 {176,177}).
- 11x96B + 81x100B. NO D-class dips.

## geometry agrees on all 3 legs
