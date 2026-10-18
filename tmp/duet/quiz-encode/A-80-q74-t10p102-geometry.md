# A-80 (Q-74): T10P102 P-head geometry — DERIVED

Bed: census cells N=52233..52324 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift.

## 1. shape: CONFIRM
- PB0 52233 sig fcb20900; PB1 52234 sig 24790908; PBA
  52235..52250 (16, sig 2479098c); single 52251 (sig
  2479090a); PBB 52252..52260 (9, SINGLE sig 24790904);
  QUAD 52261..52324 (64=4x16, SPLIT sig: rows0-2
  24790940, row3 24790944, each single). All 96B/80B.
- PBB10 VPOS [3,4,27,37-47,76,77,78,79] EXACT;
  split-sig b3 0a (52251) / 04 (PBB9).

## 2. quad rows: CONFIRM (3+1)
- M 8B pos[40,41,46,47,72,73,74,75] row-indep 16/16 x4,
  16/16 distinct, ALL NEW.
- rows0-2 share rb 1cdf25f3df7f2b; row3 unique
  9c1b81f096a42a (pos[15,27,37,38,39,44,45]).
- tails 07766cb8/b2ba6cb8/63b98cb9/53b05056; rows0,1
  share last2B 6cb8. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x13+2off) 92/92 (b5 whole set
  {152}); quad-local (0x4b+2off) 64/64, max 0xc9,
  NO wrap; b5=0x98 const 64/64.
- PBA VPOS [4,40,41,42,72,73,74,75] EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
