# A-109 (Q-103): T10R114 R-zone geometry — DERIVED

Bed: census N=57197..57452 own bed (.rav[12:-4]).
First-hand; P116-M re-derived 57133 row0 (A-108).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig da000000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[20,21,22,76,77,78,79]
  indep 256/256, 16/16 distinct. q-tab 6B EXACTLY
  pos[13,14,72,73,74,75] indep 256/256,
  16/16 distinct. 0 violations.

## 2. reuse vs P116-M: VERBATIM q FULL-6B (56th, q-carried)
- R114-Q[i] == P116-M[i] full 6B all 16,
  zero breaks (57133..57148 row0 derived).
  Heads b13,14 in place of b9,10; tails
  relocated 76..79 -> 72..75.
  NOT arithmetic, NOT novel (byte-diffs all 0).
- m-tab ALL NEW (tails 0/16 positional).
- Carry sequence now: R110 m, R111 m, R112 q,
  R113 q, R114 q.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xdb+2off)&FF 256/256; b5=0xbe+(off>=19)+
  (off>=147) 256/256 (dbl-carry, wrap-driven).
  Edges 57215->57216, 57343->57344 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
