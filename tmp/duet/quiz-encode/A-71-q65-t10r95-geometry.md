# A-71 (Q-65): T10R95 single-zone geometry — DERIVED

Bed: census cells N=50585..50840 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P97-M rows
re-derived byte-exact from 50521..50584 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 4th 100B zone. NO head singletons.
- m-tab EXACTLY pos[8,9,10,15,76,77,78,79], q-indep
  256/256, 16/16 distinct.
- q-tab EXACTLY pos[6,7,72,73,74,75], m-indep 256/256,
  16/16 distinct.

## 2. same-pos reuse 16/16 positional: CONFIRM (37th instance)
- R95-q[i] == P97-M[i] full 6B all 16 AT SAME POSITIONS
  (1st same-pos R-q reuse in 100B tier). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x33+2off)&FF 256/256; b5=0x8b+(off>=103)+
  (off>=231) 256/256 (dbl-carry).
- Edges as writer observed: 50687 255/139 -> 50688 1/140;
  50815 255/140 -> 50816 1/141 (b5 set {139,140,141}).
- varpos EXACTLY tabs+{4,5}, 68 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
