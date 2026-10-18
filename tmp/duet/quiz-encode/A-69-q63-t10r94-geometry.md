# A-69 (Q-63): T10R94 single-zone geometry — DERIVED

Bed: census cells N=50237..50492 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P96-M rows
re-derived byte-exact from 50173..50236 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 3rd 100B zone. NO head singletons.
- m-tab EXACTLY pos[44,45,46,47,72,73,74,75], q-indep
  256/256, 16/16 distinct.
- q-tab EXACTLY pos[38,39,76,77,78,79], m-indep 256/256,
  16/16 distinct.

## 2. full-6B reuse 16/16 positional: CONFIRM (36th instance)
- R94-q[i] == P96-M[i] full 6B all 16 (heads relocated
  34,35 -> 38,39; tails relocated 72..75 -> 76..79).
  Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x7b+2off)&FF 256/256; b5=0x88+(off>=67)+
  (off>=195) 256/256 (dbl-carry).
- Edges as writer observed: 50303 255/136 -> 50304 1/137;
  50431 255/137 -> 50432 1/138 (b5 set {136,137,138}).
- varpos EXACTLY tabs+{4,5}, 68 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
