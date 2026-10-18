# A-157 (Q-151): T10R138 R-zone geometry — DERIVED

Bed: census N=65549..65804 own bed (.rav[12:-4]).
First-hand; P140-M from own P140 census row0
65485..65500 (this seat); R137 m-tails re-derived
65201..65216 row0 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig e8720100 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[20,21,76,77,78,79]
  (col-tab) q-indep 256/256, 16/16 distinct,
  ALL NEW (m-tails 16/16 vs R137).
- q-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  (row-tab) m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (80th)
- R138-q[row i] == P140-M[col i] full 7B all
  16, zero breaks (q-carried, heads b13,14,15
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 16/16 novel vs P140-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x1b+2off)&FF 256/256; b5=0x00+
  (off>=115)+(off>=243) 256/256 (dbl-carry).
  Edges 65663->65664 ff/00->01/01, 65791->
  65792 ff/01->01/02 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
