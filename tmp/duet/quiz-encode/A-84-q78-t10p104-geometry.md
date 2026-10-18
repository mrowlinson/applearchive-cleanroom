# A-84 (Q-78): T10P104 P-head geometry — DERIVED

Bed: census cells N=52929..53020 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. shape: CONFIRM
- PB0 52929 sig fca20900 (96B/80B); PB1 52930 sig
  48f86c13; PBA 52931..52946 (16, 100B/84B sig
  01000000 — 1st 100B PBA, first-hand); single 52947
  (sig 48f86c13 = PB1-sig, first-hand equal); PBB
  52948..52956 (9, SINGLE sig 48f86c09); QUAD
  52957..53020 (64=4x16, SINGLE sig 48f86c8d all 4 rows).
- PBB10 VPOS [3,4,15,24-35,76,77,78,79] EXACT;
  split-sig b3 13 (52947) / 09 (PBB9).

## 2. quad rows: CONFIRM (3+1)
- M 6B pos[34,35,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- rows0-2 share rb 9e272caf96; row3 unique 99f7c74f18
  (pos[28,30,31,32,33]).
- tails 1b775126/95775126/9a785126/9ff51b7c; rows0-2
  share last2B 5126. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x83+2off) 92/92 (b5 set
  {157,158}); PBA100 b4 0x87..0xa5 no wrap, b5=0x9d
  const; quad-local (0xbb+2off) 64/64; wrap
  row2m2->m3 52991 255/157 -> 52992 1/158;
  b5=0x9d+(off>=35) 64/64.
- PBA100 VPOS [4,32,76,77,78,79] of 84B EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
