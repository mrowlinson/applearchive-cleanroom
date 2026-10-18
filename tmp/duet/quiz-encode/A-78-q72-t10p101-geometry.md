# A-78 (Q-72): T10P101 P-head geometry — DERIVED

Bed: census cells N=51885..51976 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 51885 sig 33be0900; PB1 51886 sig 24790908; PBA
  51887..51902 (16, sig 2479099a); single 51903 (sig
  24790908 = PB1-sig AGAIN, first-hand equal); PBB
  51904..51912 (9, SINGLE sig 24790904); QUAD
  51913..51976 (64=4x16, SINGLE sig 2479094c all 4
  rows). All 96B/80B.
- PBB10 VPOS [3,4,14,15,21-31,76,77,78,79] EXACT;
  split-sig b3 08 (51903) / 04 (PBB9).

## 2. quad rows: CONFIRM
- M 6B pos[28,29,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- row0==row2 rb edc4ac016f4beb; row1 unique
  8dfb6c354f14eb; row3 unique 1deb7ca92fdeea
  (pos[14,15,21,23,24,25,26]).
- tails all distinct dbf01434/b0f93705/25f99079/
  7d7c4fd1. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x5b+2off) 92/92 (b5 set
  {149,150}); quad-local (0x93+2off) 64/64; wrap
  row3m6->m7 51967 255/149 -> 51968 1/150;
  b5=0x95+(off>=55) 64/64.
- PBA VPOS [4,14,15,22,23,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
