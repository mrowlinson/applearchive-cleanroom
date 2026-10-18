# A-93 (Q-87): T10R106 R-zone geometry — DERIVED

Bed: census cells N=54413..54668 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P108-M re-derived
byte-exact from 54349..54364 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 58000000 (NEW). 15th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[20,21,22,76,77,78,79], q-indep
  256/256, 16/16 distinct. q-tab EXACTLY pos[13,14,15,
  72,73,74,75], m-indep 256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (48th)
- R106-q[i] == P108-M[i] full 7B all 16 (heads relocated
  9,10,11 -> 13,14,15; tails 76..79 -> 72..75). Zero
  breaks.

## 3. b5 rule + dips: NONE (const-count CORRECT)
- b4=(0x1b+2off)&FF 256/256; b5=0xa9+(off>=115)+
  (off>=243) 256/256 (dbl-carry). Edges 54527->54528,
  54655->54656 as writer observed.
- varpos EXACTLY tabs+{4,5} (16 var), 68 consts
  first-hand — writer "67 consts" CORRECTED. 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
