# A-151 (Q-145): T10R135 R-zone geometry — DERIVED

Bed: census N=64505..64760 own bed (.rav[12:-4]).
First-hand; P137-M re-derived 64441 row0 (A-150
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 52760000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 8B EXACTLY pos[6,7,8,9,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (77th)
- R135-q[i] == P137-M[i] full 8B all 16 (heads
  b6,7,8,9 AND tails 76..79 IN PLACE, no
  relocation -- 3rd no-relocation verbatim
  after R119/R127). Zero breaks, q-carried.
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xf3+2off)&FF 256/256; b5=0xf7+
  (off>=7)+(off>=135) 256/256 (dbl-carry).
  Edges 64511->64512 ff/f7->01/f8, 64639->
  64640 ff/f8->01/f9 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
