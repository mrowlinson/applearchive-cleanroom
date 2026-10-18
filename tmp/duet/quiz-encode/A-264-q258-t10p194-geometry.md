# A-264 (Q-258): T10P194 P-head geometry — DERIVED

Bed: census N=84249..84596 own bed (.rav[12:-4]). First-hand; P193-Q tails from own
P193 census quad row0 83929..83944 (this seat).

## 1. shape: CONFIRM
- 84249..84596 = 348/348 100B/84B exact: PB0 84249 sig 48030000 (as P193-next
  PREDICTED); PB1 84250 sig 20900600.
- PBA 84251..84266 sig 0a026900 (VPOS [4,20,21,22,23,76,77,78,79] = b4+M8
  EXACT, b5 const 0x92).
- SING 84267 sig 6fcd0700 NEW; PBB9 84268..84276 sig 10480300 NEW (VPOS
  b4+M11 b20-26,80-83 EXACT, b5 const 0x92).
- 4xOWN16 84277..84340 sigs 2db13500/0f193500/6f8d3400/a59b3600 ALL NEW (each
  VPOS [4,20,21,22,26,27,28,76,77,78,79] = b4+M10 EXACT, b5 const 0x92).
- T-RING 84341..84596 256x single sig 6f8d4803 NEW (VPOS 19 EXACT).
- Next @84597: PB0 sig 48030000 (REPEAT of own PB0!), PB1 84598 79ad0500 NEW,
  PBA 84599..84614 sig 79ad6900 NEW (VPOS [4,5,36,37,76,77,78,79] = b4,b5+M6
  EXACT — b5 VARIES {0x94,0x95} in PBA, first CONFIRM).

## 2. own-sig rows + T-ring: CONFIRM + 1 CORRECTION
- M10 POSITIONALLY shared all 4 rows 16/16 (V0 exact CONFIRM).
- CORRECTION: between-row constdiffs are 9/11/11B, not 9/11/10B. Pair 2-3
  differs at 11 const positions [0,1,2,18,19,24,25,80,81,82,83] (same set as
  pair 1-2; sig b0-2 + row-consts b18,19,24,25 + tails b80-83, all verified
  const-within-row both rows). No excludable 11th — writer miscounted.
- M-tails 16/16 distinct ALL blocks, ALL NEW vs P193Q (0/16 each, 64/64).
- T-ring TRANSPOSED (4th) CONFIRM: M8 b32-35,76-79 by COL off&15 16/16
  (heads b32,33 FULL 16/16 pairs); Q9 b24-28,72-75 by ROW off>>4 16/16.

## 3. counters + dips: CONFIRM + 1 CORRECTION, NONE
- Odd-lencode all 84249..84340: 92/92 exact.
- T-ring b4=(0xeb+2off)&FF 256/256; b5=0x92+(off>=11)+(off>=139) 256/256;
  edges 84351->84352 ff/92->01/93 + 84479->84480 ff/93->01/94.
- CORRECTION: consts are PBA 75 / PBB 72 / own-rows 73/73/73/73 / T 65 —
  own-rows are 73 not 72 (VPOS 11 = b4+M10, b5 const single-tier, 84-11=73;
  writer's own VPOS statement implies 73). PBA 75 now CORRECT (b5-inclusive
  fix verified — writer's consts() repair holds).
- PBA heads 15/16 CONFIRM (genuine, pairs==full).
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all legs modulo 2 counts (constdiff 11B, own-consts 73)
