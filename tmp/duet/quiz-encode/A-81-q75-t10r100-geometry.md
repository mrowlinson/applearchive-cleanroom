# A-81 (Q-75): T10R100 single-zone geometry — DERIVED

Bed: census cells N=52325..52580 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P102-M rows
re-derived byte-exact from 52261..52324 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 04000000 (first-hand set
  size 1). 9th 100B zone. NO head singletons.
- m-tab EXACTLY pos[6,7,12,76,77,78,79], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[44,45,50,51,72,73,74,75], m-indep
  256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (42nd instance)
- R100-q[i] == P102-M[i] full 8B all 16 (heads relocated
  40,41,46,47 -> 44,45,50,51; tails same 72..75).
  Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0xcb+2off)&FF 256/256; b5=0x98+(off>=27)+
  (off>=155) 256/256 (dbl-carry).
- Edges as writer observed: 52351 255/152 -> 52352 1/153;
  52479 255/153 -> 52480 1/154 (b5 set {152,153,154}).
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
