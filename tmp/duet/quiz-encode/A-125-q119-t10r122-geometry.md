# A-125 (Q-119): T10R122 R-zone geometry — DERIVED

Bed: census N=59981..60236 own bed (.rav[12:-4]).
First-hand; P124-M re-derived 59917 row0 (A-124
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 56050000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[20,21,22,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (64th)
- R122-q[i] == P124-M[i] full 7B all 16 (heads
  b13,14,15 IN PLACE; tails relocated 76..79 ->
  72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P124-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x9b+2off)&FF 256/256; b5=0xd4+
  (off>=51)+(off>=179) 256/256 (dbl-carry).
  Edges 60031->60032 ff/d4->01/d5, 60159->
  60160 ff/d5->01/d6 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
