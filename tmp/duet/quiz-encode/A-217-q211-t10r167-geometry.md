# A-217 (Q-211): T10R167 R-zone geometry — DERIVED

Bed: census N=75641..75896 own bed (.rav[12:-4]).
First-hand; P169-M from own P169 census row0
75577..75592 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 37732500 NEW
  (== predicted next-tier sig from Q-210).
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE, 0 overlap vs P169M).
- q-tab 7B EXACTLY pos[6,7,9,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (109th)
- R167-q[i] == P169-M[i] full 7B all 16,
  zero breaks (heads b6,7,9 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xf3+2off)&FF 256/256; b5=0x4e+
  (off>=7)+(off>=135) 256/256 (dbl-carry,
  step positions 7/135 exact).
  Edges 75647->75648 ff/4e->01/4f, 75775->
  75776 ff/4f->01/50 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.
- Next tier @75897 sig 25000000.

## geometry agrees on all 3 legs
