# A-65 (Q-59): T10R92 single-zone geometry — DERIVED

Bed: census cells N=49541..49796 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P94-M rows
re-derived byte-exact from 49493..49540.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 1st 100B zone. NO head singletons.
- m-tab EXACTLY pos[6,7,12,76,77,78,79], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[44,45,50,51,72,73,74,75], m-indep
  256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (34th instance)
- R92-q[i] == P94-M[i] full 8B byte-for-byte all 16
  (P94M re-derived first-hand from quad 3x16, 16/16
  distinct; heads relocated 40,41,46,47 -> 44,45,50,51;
  tails same 72..75). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x0b+2off)&FF 256/256; b5=0x83+(off>=123)+
  (off>=251) 256/256 (dbl-carry).
- Edges as writer observed: 49663 255/131 -> 49664 1/132;
  49791 255/132 -> 49792 1/133 (b5 set {131,132,133}).
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
