# A-141 (Q-135): T10R130 R-zone geometry — DERIVED

Bed: census N=62765..63020 own bed (.rav[12:-4]).
First-hand; P132-M re-derived 62701 row0 (A-140
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig ab0a0000 NEW
  (ab-kin to P132-quad ab000000). NO head
  singletons.
- m-tab 6B EXACTLY pos[20,21,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (72nd)
- R130-q[i] == P132-M[i] full 7B all 16 (heads
  b13,14,15 IN PLACE; tails relocated 76..79 ->
  72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P132-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x5b+2off)&FF 256/256; b5=0xea+
  (off>=83)+(off>=211) 256/256 (dbl-carry).
  Edges 62847->62848 ff/ea->01/eb, 62975->
  62976 ff/eb->01/ec as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
