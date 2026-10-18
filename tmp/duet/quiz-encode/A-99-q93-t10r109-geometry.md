# A-99 (Q-93): T10R109 R-zone geometry — DERIVED

Bed: census cells N=55457..55712 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P111-M re-derived
byte-exact from 55393..55408 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig be000000 (NEW). 18th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[26,27,76,77,78,79], q-indep
  256/256, 16/16 distinct. q-tab EXACTLY pos[20,21,22,
  72,73,74,75], m-indep 256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (51st)
- R109-q[i] == P111-M[i] full 7B all 16 (heads b20,21,22
  IN PLACE; tails 76..79 -> 72..75). Zero breaks.

## 3. b5 rule + dips: NONE (const-count CORRECT)
- b4=(0x43+2off)&FF 256/256; b5=0xb1+(off>=95)+
  (off>=223) 256/256 (dbl-carry). Edges 55551->55552,
  55679->55680 as writer observed.
- varpos EXACTLY tabs+{4,5} (15 var), 69 consts
  first-hand — writer "67 consts" CORRECTED. 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
