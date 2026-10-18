# A-195 (Q-189): T10R156 R-zone geometry — DERIVED

Bed: census N=71813..72068 own bed (.rav[12:-4]).
First-hand; P158-M from own P158 census row0
71749..71764 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 36a00700 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[6,7,8,9,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,
  75] m-indep 256/256, 16/16 distinct (1st
  8B q-tab).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (98th)
- R156-q[i] == P158-M[i] full 8B all 16,
  zero breaks (q-carried, heads b48-51 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P158-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x0b+2off)&FF 256/256; b5=0x31+
  (off>=123)+(off>=251) 256/256 (dbl-carry).
  Edges 71935->71936 ff/31->01/32, 72063->
  72064 ff/32->01/33 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
