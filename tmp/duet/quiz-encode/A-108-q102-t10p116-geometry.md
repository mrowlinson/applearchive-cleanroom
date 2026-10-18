# A-108 (Q-102): T10P116 P-head geometry — DERIVED

Bed: census N=57105..57196 own bed (.rav[12:-4]).
First-hand; P115-M own bed present (A-106).

## 1. shape: CONFIRM
- PB0 57105 96B/80B sig 003f9501 NEW; PB1 57106
  100B/84B sig 02000000; PBA 57107..57122 (16,
  100B/84B sig 24000000 NEW); 57123 single
  100B/84B sig 01000000; 57124..57132 (9, 96B/80B
  sig 25809fda, split-sig pair like P106); QUAD
  57133..57196 (64=4x16, ALL 100B/84B, SINGLE
  sig 0d000000 NEW). 10x96B + 82x100B.
- PBA VPOS [4,6,7,76-79] EXACT; PBB9-9 VPOS
  [4,6,7,8,9,10,11,76-79] EXACT; QUAD VPOS
  [4,6,7,9,10,12,13,14,76-83] EXACT.

## 2. quad rows: CONFIRM + M-novelty ANSWERED
- M 6B pos[9,10,76,77,78,79] col-indep 64/64,
  16/16 distinct x4. NEW 6B layout.
- row-bytes b6,7,12,13,14 EXACT as writer:
  row0==row1==row3 4edcbdee10, row2 unique
  0b5b65e732.
- tails b80..83 row-const d617d879/4118d879/
  4fdd1d92/cf4f507f all distinct.
- PBA M 6B pos[6,7,76-79] 16/16 distinct NEW;
  PBB9 M 10B pos[6-11,76-79] 9/9 distinct NEW.
- M-novelty vs P115-M: ALL NEW first-hand (0/16
  tails, 0/16 heads overlap; 6B vs 7B layout).

## 3. counters + dips: CONFIRM, NONE
- b4=(0x23+2off) 92/92, b5=0xbe const 92/92,
  no wrap, whole tier.
- 10x96B + 82x100B. NO D-class dips.

## geometry agrees on all 3 legs
