# A-177 (Q-171): T10R148 R-zone geometry — DERIVED

Bed: census N=69029..69284 own bed (.rav[12:-4]).
First-hand; P150-M from own P150 census row0
68965..68980 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 53da0300 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[6,7,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[48,49,50,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (90th)
- R148-q[i] == P150-M[i] full 7B all 16,
  zero breaks (q-carried, heads b48,49,50
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P150-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x4b+2off)&FF 256/256; b5=0x1b+
  (off>=91)+(off>=219) 256/256 (dbl-carry).
  Edges 69119->69120 ff/1b->01/1c, 69247->
  69248 ff/1c->01/1d as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
