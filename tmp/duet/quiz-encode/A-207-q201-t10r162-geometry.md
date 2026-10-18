# A-207 (Q-201): T10R162 R-zone geometry — DERIVED

Bed: census N=73901..74156 own bed (.rav[12:-4]).
First-hand; P164-M from own P164 census row0
73837..73852 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig fff00800 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[20,21,22,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 9B EXACTLY pos[13,14,15,16,17,72,73,
  74,75] m-indep 256/256, 16/16 distinct
  (1st 9B q-tab).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (104th)
- R162-q[i] == P164-M[i] full 9B all 16,
  zero breaks (q-carried, heads b13-17 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P164-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x5b+2off)&FF 256/256; b5=0x41+
  (off>=83)+(off>=211) 256/256 (dbl-carry).
  Edges 73983->73984 ff/41->01/42, 74111->
  74112 ff/42->01/43 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
