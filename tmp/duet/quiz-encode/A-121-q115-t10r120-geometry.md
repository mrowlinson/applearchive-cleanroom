# A-121 (Q-115): T10R120 R-zone geometry — DERIVED

Bed: census N=59285..59540 own bed (.rav[12:-4]).
First-hand; P122-M re-derived 59221 row0 (A-120
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig e4010000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[32,33,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 7B EXACTLY pos[18,26,27,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (62nd)
- R120-q[i] == P122-M[i] full 7B all 16 (heads
  b18,26,27 IN PLACE; tails relocated 76..79 ->
  72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P122-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x2b+2off)&FF 256/256; b5=0xcf+
  (off>=107)+(off>=235) 256/256 (dbl-carry).
  Edges 59391->59392 ff/cf->01/d0, 59519->
  59520 ff/d0->01/d1 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
