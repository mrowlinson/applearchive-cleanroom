# A-211 (Q-205): T10R164 R-zone geometry — DERIVED

Bed: census N=74597..74852 own bed (.rav[12:-4]).
First-hand; P166-M from own P166 census row0
74533..74548 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 95091000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[6,7,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,
  75] m-indep 256/256, 16/16 distinct (3rd
  8B q-tab).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (106th)
- R164-q[i] == P166-M[i] full 8B all 16,
  zero breaks (q-carried, heads b48-51 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P166-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xcb+2off)&FF 256/256; b5=0x46+
  (off>=27)+(off>=155) 256/256 (dbl-carry).
  Edges 74623->74624 ff/46->01/47, 74751->
  74752 ff/47->01/48 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
