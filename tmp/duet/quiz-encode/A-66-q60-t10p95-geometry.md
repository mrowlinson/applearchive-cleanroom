# A-66 (Q-60): T10P95 P-head geometry — DERIVED

Bed: census cells N=49797..49888 on disk (own bed, payload
.rav[12:-4]). All 80B (P-head back to 80B after 100B R92).
First-hand this shift.

## 1. shape: CONFIRM
- PB0 49797 sig ad550300; PB1 49798 sig 4aad5503; PBA
  49799..49814 (16, sig aed45a35); PBB 49815..49824 (10,
  SIG-VARIEGATED in writer's exact cell order: c97c4801/
  067c9201/2f3c2201x2/067c9201x2/cfbcb001/ab7cb601/
  cfbcb001/323c2201); QUAD 49825..49888 (64=4x16, SPLIT
  sig rows0-2 067c921a, row3 323c221a). All 96B/80B.

## 2. quad M shared x4: CONFIRM
- M 7B pos[13,18,19,72,73,74,75] row-indep 16/16 x4
  (row3 same M despite unique sig), 16/16 distinct.
- rows0-2 b16,17=d1,89 + tails 5e7b0ab6/e67b0ab6/
  9ff00ab6 (last2B 0ab6 shared); row3 b16,17=ca,41
  tail 3bb27bcf. All single-valued per row.

## 3. counters + dips: CONFIRM, NONE
- b4 whole-tier linear (0x0b+2off) 92/92 no wrap;
  quad-local (0x43+2off) 64/64.
- b5 = 0x85 const whole tier 92/92 (quad 64/64).
- PBA VPOS [4,13,14,15,72,73,74,75]; PBB VPOS
  [0,1,2,4,16,17,18,76,77,78,79] — both EXACT.
  NO D-class dips.

## geometry agrees on all 3 legs
