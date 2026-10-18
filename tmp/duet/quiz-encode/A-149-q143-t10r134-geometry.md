# A-149 (Q-143): T10R134 R-zone geometry — DERIVED

Bed: census N=64157..64412 own bed (.rav[12:-4]).
First-hand; P136-M re-derived 64093 row0 (A-148
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig f5510000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[44,45,46,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 8B EXACTLY pos[32,33,38,39,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (76th)
- R134-q[i] == P136-M[i] full 8B all 16 (heads
  b32,33,38,39 IN PLACE; tails relocated 76..79
  -> 72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P136-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x3b+2off)&FF 256/256; b5=0xf5+
  (off>=99)+(off>=227) 256/256 (dbl-carry).
  Edges 64255->64256 ff/f5->01/f6, 64383->
  64384 ff/f6->01/f7 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
