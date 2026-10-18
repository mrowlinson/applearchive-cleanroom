# A-79 (Q-73): T10R99 single-zone geometry — DERIVED

Bed: census cells N=51977..52232 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P101-M rows
re-derived byte-exact from 51913..51976 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 04000000 (NEW sig,
  first-hand set size 1). 8th 100B zone. NO head singletons.
- m-tab EXACTLY pos[38,39,76,77,78,79], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[32,33,72,73,74,75], m-indep 256/256,
  16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (41st instance)
- R99-q[i] == P101-M[i] full 6B all 16 (heads relocated
  28,29 -> 32,33; tails same 72..75). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x13+2off)&FF 256/256; b5=0x96+(off>=119)+
  (off>=247) 256/256 (dbl-carry).
- Edges as writer observed: 52095 255/150 -> 52096 1/151;
  52223 255/151 -> 52224 1/152 (b5 set {150,151,152}).
- varpos EXACTLY tabs+{4,5}, 70 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
