# A-102 (Q-96): T10P113 P-head geometry — DERIVED

Bed: census N=56061..56152 own bed (.rav[12:-4]).
First-hand this shift.

## 1. shape: CONFIRM (9-cell PBB + extra fat singleton real)
- PB0 56061 96B sig 029a7701 NEW; PB1 56062 100B
  fat 01000000 (5th); PBA 56063..56078 (16, 100B/84B
  sig 16000000 NEW); SINGLETON 56079 100B fat
  01000000; PBB 56080..56088 (9 ONLY, 96B/80B sig
  0e7851a3); QUAD 56089..56152 (64=4x16, ALL 100B/84B,
  SINGLE sig 0a000000 NEW, 5th consecutive).
- PBA VPOS [4,5,48,49,50,76-79] EXACT (b5 step
  inside PBA); PBB VPOS [4,40-43,45-47,76-79] EXACT.
- 10x96B + 82x100B.

## 2. quad rows: CONFIRM
- M 7B pos[6,7,12,76,77,78,79] row-indep 16/16 x4,
  16/16 distinct; b76-79 per-byte distinct 16/14/15/16.
- coarse R-band b44-47,49-51 row-only 2-val:
  rows0,1,3 28cfa19c10b7c7, row2 880534a470c55f.
- tails b80..83 row-const 057ac659/747ac659/
  f971e38c/507bc659 (per-byte 4/3/2/2 distinct).
- PBA M 7B pos[48,49,50,76-79] 16/16; PBB M 11B
  pos[40-43,45-47,76-79] 9/9.

## 3. counters + dips: CONFIRM, NONE
- tier b4=(0xfb+2off) 92/92; PBA b4=(0xff+2i) 16/16,
  b5 0xb5->0xb6 at 56064 (i=1) then const.
- quad b4=(0x33+2off) 64/64, b5=0xb6 const 64/64.
  NO D-class dips.

## geometry agrees on all 3 legs
