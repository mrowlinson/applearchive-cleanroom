# A-129 (Q-123): T10R124 R-zone geometry — DERIVED

Bed: census N=60677..60932 own bed (.rav[12:-4]).
First-hand; P126-M re-derived 60613 row0 (A-128
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 32040000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[6,7,8,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (66th)
- R124-q[i] == P126-M[i] full 8B all 16 (heads
  b48,49,50,51 IN PLACE; tails relocated 76..79
  -> 72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P126-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x0b+2off)&FF 256/256; b5=0xda+
  (off>=123)+(off>=251) 256/256 (dbl-carry).
  Edges 60799->60800 ff/da->01/db, 60927->
  60928 ff/db->01/dc as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
