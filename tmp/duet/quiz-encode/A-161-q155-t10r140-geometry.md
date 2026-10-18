# A-161 (Q-155): T10R140 R-zone geometry — DERIVED

Bed: census N=66245..66500 own bed (.rav[12:-4]).
First-hand; P142-M from own P142 census row0
66181..66196 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 324d0100 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[6,7,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[48,49,50,72,73,74,75]
  m-indep 256/256, 16/16 distinct (b50 =
  0x67 rows0-14, 0xcf row15 exact).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (82nd)
- R140-q[i] == P142-M[i] full 7B all 16,
  zero breaks (q-carried, heads b48,49,50
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P142-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x8b+2off)&FF 256/256; b5=0x05+
  (off>=59)+(off>=187) 256/256 (dbl-carry).
  Edges 66303->66304 ff/05->01/06, 66431->
  66432 ff/06->01/07 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
