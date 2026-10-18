# A-219 (Q-213): T10R168 R-zone geometry — DERIVED

Bed: census N=75989..76244 own bed (.rav[12:-4]).
First-hand; P170-M from own P170 census row0
75925..75940 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 64df2500 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails RELOCATED 76..79 -> 72..75, 1st
  m-relocation; m-tab carries no 76..79).
- q-tab 6B EXACTLY pos[26,27,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (110th)
- R168-q[i] == P170-M[i] full 6B all 16,
  zero breaks (FULLY IN PLACE b26,27,76-79,
  1st no-relocation carry).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xab+2off)&FF 256/256; b5=0x51+
  (off>=43)+(off>=171) 256/256 (dbl-carry).
  Edges 76031->76032 ff/51->01/52, 76159->
  76160 ff/52->01/53 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.
- Next tier @76245 sig 25000000 (2nd
  same-PB0-sig).

## geometry agrees on all 3 legs
