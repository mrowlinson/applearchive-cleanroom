# A-85 (Q-79): T10R102 single-zone geometry — DERIVED

Bed: census cells N=53021..53276 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P104-M rows
re-derived byte-exact from 52957..53020 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 08000000 (NEW,
  first-hand set size 1). 11th 100B zone. NO head singletons.
- m-tab EXACTLY pos[44,45,46,72,73,74,75], q-indep
  256/256, 16/16 distinct.
- q-tab EXACTLY pos[38,39,76,77,78,79], m-indep 256/256,
  16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (45th instance)
- R102-q[i] == P104-M[i] full 6B all 16 (heads relocated
  34,35 -> 38,39; tails relocated 72..75 -> 76..79).
  Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x3b+2off)&FF 256/256; b5=0x9e+(off>=99)+
  (off>=227) 256/256 (dbl-carry, wrap-driven).
- Edges as writer observed: 53119 255/158 -> 53120 1/159;
  53247 255/159 -> 53248 1/160 (b5 set {158,159,160}).
- varpos EXACTLY tabs+{4,5}, 69 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
