# A-89 (Q-83): T10R104 R-zone geometry — DERIVED

Bed: census cells N=53717..53972 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P106-M re-derived
byte-exact from 53653..53668 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 48000000 (NEW). 13th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[32,33,34,76,77,78,79], q-indep
  256/256, 16/16 distinct. q-tab EXACTLY pos[18,19,26,
  27,72,73,74,75], m-indep 256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (47th)
- R104-q[i] == P106-M[i] full 8B all 16 (tails relocated
  76..79 -> 72..75). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0xab+2off)&FF 256/256; b5=0xa3+(off>=43)+
  (off>=171) 256/256 (dbl-carry). Edges 53759->53760,
  53887->53888 as writer observed.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
