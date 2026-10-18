# A-163 (Q-157): T10R141 R-zone geometry — DERIVED

Bed: census N=66593..66848 own bed (.rav[12:-4]).
First-hand; P143-M from own P143 census row0
66529..66544 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 9a7a0100 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[19,26,27,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[20,21,22,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (83rd)
- R141-q[i] == P143-M[i] full 7B all 16,
  zero breaks (q-carried, heads b20,21,22
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P143-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x43+2off)&FF 256/256; b5=0x08+
  (off>=95)+(off>=223) 256/256 (dbl-carry).
  Edges 66687->66688 ff/08->01/09, 66815->
  66816 ff/09->01/0a as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
