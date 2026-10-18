# A-111 (Q-105): T10R115 R-zone geometry — DERIVED

Bed: census N=57545..57800 own bed (.rav[12:-4]).
First-hand; P117-M re-derived 57481 row0 (A-110).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig dc000000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[30,31,38,39,76,77,78,79]
  indep 256/256, 16/16 distinct, ALL NEW.
  q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  indep 256/256, 16/16 distinct. 0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (57th, q-carried)
- R115-Q[i] == P117-M[i] full 7B all 16,
  zero breaks (57481..57496 row0 derived).
  Heads b32,33,34 IN PLACE; tails relocated
  76..79 -> 72..75.
- NOT arithmetic, NOT novel (byte-diffs all 0).
- m-tab ALL NEW (tails 0/16 positional).
- Carry sequence now: R110 m, R111 m, R112 q,
  R113 q, R114 q, R115 q.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x93+2off)&FF 256/256; b5=0xc1+(off>=55)+
  (off>=183) 256/256 (dbl-carry, wrap-driven).
  Edges 57599->57600, 57727->57728 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
