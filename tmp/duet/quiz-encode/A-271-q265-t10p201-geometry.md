# A-271 (Q-265): T10P201 P-head geometry — DERIVED

Bed: census N=86685..87032 own bed (.rav[12:-4]). First-hand; P200-T tails from own
P200 census (M-by-col tails 86429..86444, this seat).

## 1. shape: CONFIRM
- 86685..87032 = 348/348 100B/84B exact: PB0 86685 sig 74030000 (REPEAT of
  P200 PB0 PREDICTED-exact); PB1 86686 sig 51de0500 (repeat).
- PBA 86687..86702 sig 51de6d00 (repeat; VPOS [4,48,49,50,51,76,77,78,79] =
  b4+M8 EXACT, b5 const).
- PBB SPLIT 2+7 (86703..86704 + 86706..86712) sig 51de0500 (== PB1; joint
  VPOS b4+M13 b23,35,45-51,80-83 EXACT; 9-diverge 9/9; b5 const 0xa5).
- SING 86705 gap sig bb090300 NEW.
- QUAD 86713..86776 single sig 16e55d00 NEW (VPOS 18 EXACT = b4+M6+R7+tails,
  b5 const 0xa5).
- T-RING 86777..87032 256x single sig 6f51de05 NEW (VPOS 14 EXACT).
- Next @87033: PB0 sig 9e030000 NEW, PB1 87034 7c3d0700 NEW, PBA 87035..87036
  sig c8d77300 NEW (probed 2 cells).

## 2. quad + T-ring: CONFIRM
- Quad M6 b6,7,76-79: row-indep 16/16 x4, shared 16/16 (heads b6,7 FULL
  16/16 pairs).
- R7 b35,46-51: all 4 distinct, no pairing (62bbbe71e6e7f0 / 422a06f1c597d3
  / 422a0611c697d3 / 422a0631c697d3).
- Tails 4/4 distinct (70c03488/d92ded29/3cd8ec1c/b7e39d1e), 16/16 bytes
  (true no-sharing CONFIRM).
- M-tails ALL NEW vs P200T (0/16).
- T-ring TRANSPOSED (11th) CONFIRM: M6 b13,14,76-79 by COL off&15 16/16; Q6
  b6,7,72-75 by ROW off>>4 16/16.

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 86685..86776: 92/92 exact.
- T-ring b4=(0xf3+2off)&FF 256/256; b5=0xa5+(off>=7)+(off>=135) 256/256;
  edges 86783->86784 ff/a5->01/a6 + 86911->86912 ff/a6->01/a7.
- Consts (84-VPOS) ALL 4 EXACT: PBA 75, PBB 70 (joint), quad 66 (b5-in), T 70.
- varpos partitioned exact throughout, 0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
