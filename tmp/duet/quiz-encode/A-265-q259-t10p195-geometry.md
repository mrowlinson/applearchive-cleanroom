# A-265 (Q-259): T10P195 P-head geometry — DERIVED

Bed: census N=84597..84944 own bed (.rav[12:-4]). First-hand; P194-T tails from own
P194 census (M-by-col tails 84341..84356, this seat).

## 1. shape: CONFIRM
- 84597..84944 = 348/348 100B/84B exact: PB0 84597 sig 48030000 (REPEAT of
  P194 PB0 PREDICTED-exact); PB1 84598 sig 79ad0500.
- PBA 84599..84614 sig 79ad6900 (VPOS [4,5,36,37,76,77,78,79] = b4,b5+M6
  EXACT — b5 CARRY 0x94->0x95 @84608: 84607 ff/94 -> 84608 01/95, lencode,
  NOT const CONFIRM).
- PBB SPLIT 2+7 (84615..84616 + 84618..84624) sig 79ad0500 (== PB1; joint
  VPOS b4+M12 b32,33,37-42,80-83 EXACT; 9-diverge 9/9 distinct; b5 const
  0x95).
- SING 84617 gap sig d3dd0300 NEW.
- QUAD 84625..84688 single sig 79ad7900 NEW (VPOS 18 EXACT =
  b4,b34,b36-43,76-79,80-83; b5 const 0x95 whole quad).
- T-RING 84689..84944 256x single sig 79ad9906 NEW (VPOS 17 EXACT =
  b4,b5+M8+Q7; count 256/256 verified over 4 independent first-hand reads —
  one initial read transiently returned the P193 T-ring sig, unreproducible;
  bed mtimes stable since own census, writer's sig CONFIRMED).
- Next @84945: PB0 sig 48030000 (REPEAT own!), PB1 84946 79ad0500 (repeat),
  PBA 84947..84948 sig 97d75a00 NEW (probed 2 cells, both match).

## 2. quad + T-ring: CONFIRM (+1 axis clarification)
- Quad M5 b43,76-79: row-indep 16/16 x4, shared 16/16.
- b42 ROW-RULE 16/16 cols (64/64): base even, r0/r1 identity, r2 = base|1,
  r3 = base^2 — all 16 columns exact.
- b34 HALF-rule values CONFIRM (0x17 / 0x1f) with AXIS CLARIFICATION: halves
  are COLUMNS (m0-7 = 0x17, m8-15 = 0x1f), all 4 rows identical — NOT row
  halves (each row-half contains both values).
- R6 b36-41 TOP-PAIRED r0==r1 0d5ab393900c (3/4 distinct: r2 4d5d6b8fd05b,
  r3 785bb32550d5).
- Tails 4/4 distinct (eb851082/21861082/f6a013ce/5162ddea), 14/16 bytes.
- M-tails ALL NEW vs P194T (0/16).
- T-ring TRANSPOSED (5th) + TAILS-SWAPPED (2nd) CONFIRM: M8 b48-51,72-75 by
  COL off&15 16/16; Q7 b34,42,43,76-79 by ROW off>>4 16/16; normal frame
  M-rows 0/16 refuted.

## 3. counters + dips: CONFIRM + 2 CORRECTIONS, NONE
- Odd-lencode all 84597..84688: 92/92 exact.
- T-ring b4=(0xa3+2off)&FF 256/256; b5=0x95+(off>=47)+(off>=175) 256/256;
  edges 84735->84736 ff/95->01/96 + 84863->84864 ff/96->01/97.
- CORRECTIONS: consts are 76/71/66/67, not 76/72/65/67 — PBB VPOS is 13
  (b4+M12) so 84-13=71 (writer's 72 contradicts their own M12); quad VPOS is
  18 (b5 const) so 84-18=66 (writer's leg-3 "84-19" contradicts their own
  leg-1 VPOS 18). PBA 76 + T 67 CONFIRM.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all legs modulo 2 consts (PBB 71, quad 66) + b34 axis
