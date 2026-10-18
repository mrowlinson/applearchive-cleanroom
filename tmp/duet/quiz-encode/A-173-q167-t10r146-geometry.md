# A-173 (Q-167): T10R146 R-zone geometry — DERIVED

Bed: census N=68333..68588 own bed (.rav[12:-4]).
First-hand; P148-M from own P148 census row0
68269..68284 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 42690300 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[20,21,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (88th)
- R146-q[i] == P148-M[i] full 7B all 16,
  zero breaks (q-carried, heads b13,14,15
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P148-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xdb+2off)&FF 256/256; b5=0x15+
  (off>=19)+(off>=147) 256/256 (dbl-carry).
  Edges 68351->68352 ff/15->01/16, 68479->
  68480 ff/16->01/17 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
