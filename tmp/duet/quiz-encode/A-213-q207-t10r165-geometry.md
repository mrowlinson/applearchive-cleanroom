# A-213 (Q-207): T10R165 R-zone geometry — DERIVED

Bed: census N=74945..75200 own bed (.rav[12:-4]).
First-hand; P167-M from own P167 census row0
74881..74896 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c9da1100 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[19,26,27,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 8B EXACTLY pos[20,21,22,23,72,73,74,
  75] m-indep 256/256, 16/16 distinct (4th
  8B q-tab).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (107th)
- R165-q[i] == P167-M[i] full 8B all 16,
  zero breaks (q-carried, heads b20-23 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P167-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x83+2off)&FF 256/256; b5=0x49+
  (off>=63)+(off>=191) 256/256 (dbl-carry).
  Edges 75007->75008 ff/49->01/4a, 75135->
  75136 ff/4a->01/4b as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
