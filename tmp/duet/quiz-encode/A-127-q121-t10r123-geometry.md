# A-127 (Q-121): T10R123 R-zone geometry — DERIVED

Bed: census N=60329..60584 own bed (.rav[12:-4]).
First-hand; P125-M re-derived 60265 row0 (A-126
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 30040000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[38,39,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (65th)
- R123-q[i] == P125-M[i] full 7B all 16 (heads
  b32,33,34 IN PLACE; tails relocated 76..79 ->
  72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P125-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x53+2off)&FF 256/256; b5=0xd7+
  (off>=87)+(off>=215) 256/256 (dbl-carry).
  Edges 60415->60416 ff/d7->01/d8, 60543->
  60544 ff/d8->01/d9 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
