# A-209 (Q-203): T10R163 R-zone geometry — DERIVED

Bed: census N=74249..74504 own bed (.rav[12:-4]).
First-hand; P165-M from own P165 census row0
74185..74200 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 41571100 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[38,39,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (105th)
- R163-q[i] == P165-M[i] full 7B all 16,
  zero breaks (q-carried, heads b32,33,34
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P165-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x13+2off)&FF 256/256; b5=0x44+
  (off>=119)+(off>=247) 256/256 (dbl-carry).
  Edges 74367->74368 ff/44->01/45, 74495->
  74496 ff/45->01/46 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
