# A-147 (Q-141): T10R133 R-zone geometry — DERIVED

Bed: census N=63809..64064 own bed (.rav[12:-4]).
First-hand; P135-M re-derived 63745 row0 (A-146
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig b9500000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[26,27,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 6B EXACTLY pos[20,21,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (75th)
- R133-q[i] == P135-M[i] full 6B all 16 (heads
  b20,21 IN PLACE; tails relocated 76..79 ->
  72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P135-M tails.

## 3. b5 rule + dips: CORRECT consts 69->70, else CONFIRM
- b4=(0x83+2off)&FF 256/256; b5=0xf2+
  (off>=63)+(off>=191) 256/256 (dbl-carry).
  Edges 63871->63872 ff/f2->01/f3, 63999->
  64000 ff/f3->01/f4 as writer.
- varpos EXACTLY tabs+{4,5}, 0 stragglers --
  but consts = 70, NOT 69 (12 tab + 2 counter
  = 14 varpos; 84-14 = 70). NO D-class dips.

## legs 1-2 agree; leg3 CORRECTS const count
