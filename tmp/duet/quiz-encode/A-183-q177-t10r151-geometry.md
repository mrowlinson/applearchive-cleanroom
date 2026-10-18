# A-183 (Q-177): T10R151 R-zone geometry — DERIVED

Bed: census N=70073..70328 own bed (.rav[12:-4]).
First-hand; P153-M from own P153 census row0
70009..70024 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 783c0300 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[6,7,9,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (93rd)
- R151-q[i] == P153-M[i] full 7B all 16,
  zero breaks (q-carried, heads b6,7,9 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P153-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x73+2off)&FF 256/256; b5=0x23+
  (off>=71)+(off>=199) 256/256 (dbl-carry).
  Edges 70143->70144 ff/23->01/24, 70271->
  70272 ff/24->01/25 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
