# A-75 (Q-69): T10R97 single-zone geometry — DERIVED

Bed: census cells N=51281..51536 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P99-M rows
re-derived byte-exact from 51217..51280 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 6th 100B zone. NO head singletons.
- m-tab EXACTLY pos[42,43,50,51,76,77,78,79], q-indep
  256/256, 16/16 distinct.
- q-tab EXACTLY pos[44,45,46,72,73,74,75], m-indep
  256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (39th instance)
- R97-q[i] == P99-M[i] full 7B all 16 (heads relocated
  40,41,42 -> 44,45,46; tails same 72..75). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0xa3+2off)&FF 256/256; b5=0x90+(off>=47)+
  (off>=175) 256/256 (dbl-carry).
- Edges as writer observed: 51327 255/144 -> 51328 1/145;
  51455 255/145 -> 51456 1/146 (b5 set {144,145,146}).
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
