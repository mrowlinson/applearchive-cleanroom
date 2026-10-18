# A-273 (viewer r3): Q-267 T10P203 P-head @87381 — CONFIRM all 3

First-hand bed 87381..87732 (regen RC=0
missing=0; q267.py + swap probe).

## 1. shape: CONFIRM
- 348 cells sizes {(100,84)}. PB0 9e030000
  (REPEAT of P202 PB0 PREDICTED-exact), PB1
  95020500, PBA 95027100 (VPOS 7 exact
  b4+M6 b36,37,76-79, b5 const), PBB10
  95020500 ==PB1 (VPOS 13 exact b4+M12
  b32,33,37-42,80-83, b5 const, 10-diverge),
  QUAD 95026d00 (VPOS 21 exact, b5 carry
  off15: 87423 ff/aa -> 87424 01/ab),
  T-RING 95022d07 (VPOS 19).
- Next @87729 3c070000 NEW + 87730 95020d00
  NEW + 87731/32 5629d000 NEW.

## 2. quad + T-ring: CONFIRM
- Quad M8 b23,34,35,43,76-79: rows full 16
  x4, positional shared 16/16 x3 vs row0.
- b42 RULE cols 16/16 (base-even, r0==r1,
  r2==r3==base-1; 64/64 cells).
- R6 b36-41 DOUBLE-paired r0==r1
  fcde31b59093 + r2==r3 b5ddcf971004 (2/4
  distinct, first double-pair).
- Tails 4/4 distinct, 13/16 bytes.
- M-tails 16/16 ALL NEW vs P202T (0
  shared; staged label inverted, value
  exact).
- T-ring TRANSPOSED (13th) + TAILS-SWAPPED
  (4th): M8 b48-51,72-75 by COL 16/16, Q9
  b23,34,35,42,43,76-79 by ROW 16/16;
  swap: ring-Q common-8B rows positional
  == quad-M row0 16/16, set 16/16.

## 3. counters + dips: CONFIRM, NONE
- Odd-lencode all 87381..87472: 92/92 exact.
- T-ring b4=(0x63+2off)&FF 256/256;
  b5=0xab+(off>=79)+(off>=207) 256/256;
  edges 87551->87552 ff/ab->01/ac +
  87679->87680 ff/ac->01/ad.
- Consts (84-VPOS) ALL 4 EXACT: PBA 77, PBB
  71, quad 63, T 65.
- varpos partitioned exact throughout, 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
