# A-223 (Q-217): T10R170 R-zone geometry — DERIVED

Bed: census N=76685..76940 own bed (.rav[12:-4]).
First-hand; P172-M from own P172 census row0
76621..76636 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 63755000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[20,21,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 8B EXACTLY pos[13,14,15,16,72,73,74,
  75] m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (112th)
- R170-q[i] == P172-M[i] full 8B all 16,
  zero breaks (heads b13-16 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x1b+2off)&FF 256/256; b5=0x57+
  (off>=115)+(off>=243) 256/256 (dbl-carry).
  Edges 76799->76800 ff/57->01/58, 76927->
  76928 ff/58->01/59 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.
- Next tier @76941: PB0 50000000, PB1
  eaa00000, PBA ad2a0b00 (prediction exact).

## geometry agrees on all 3 legs
