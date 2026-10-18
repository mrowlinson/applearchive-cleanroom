# A-95 (Q-89): T10R107 R-zone geometry — DERIVED

Bed: census cells N=54761..55016 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P109-M re-derived
byte-exact from 54697..54712 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig b2000000 (NEW). 16th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[30,31,38,39,76,77,78,79], q-indep
  256/256, 16/16 distinct. q-tab EXACTLY pos[32,33,72,
  73,74,75], m-indep 256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (49th)
- R107-q[i] == P109-M[i] full 6B all 16 (heads b32,33 IN
  PLACE; tails 76..79 -> 72..75). Zero breaks.

## 3. b5 rule + dips: NONE (const-count CORRECT)
- b4=(0xd3+2off)&FF 256/256; b5=0xab+(off>=23)+
  (off>=151) 256/256 (dbl-carry). Edges 54783->54784,
  54911->54912 as writer observed.
- varpos EXACTLY tabs+{4,5} (16 var), 68 consts
  first-hand — writer "66 consts" CORRECTED. 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
