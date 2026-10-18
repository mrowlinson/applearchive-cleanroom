# A-145 (Q-139): T10R132 R-zone geometry — DERIVED

Bed: census N=63461..63716 own bed (.rav[12:-4]).
First-hand; P134-M re-derived 63397 row0 (A-144
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 643a0000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[6,7,8,9,76,77,78,79]
  (widest m-tab) q-indep 256/256, tuple 16/16
  distinct, ALL NEW (m-tails 0/16 vs prior-R
  m-tails).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (74th)
- R132-q[i] == P134-M[i] full 8B all 16 (heads
  b48,49,50,51 IN PLACE; tails relocated 76..79
  -> 72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P134-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xcb+2off)&FF 256/256; b5=0xef+
  (off>=27)+(off>=155) 256/256 (dbl-carry).
  Edges 63487->63488 ff/ef->01/f0, 63615->
  63616 ff/f0->01/f1 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
