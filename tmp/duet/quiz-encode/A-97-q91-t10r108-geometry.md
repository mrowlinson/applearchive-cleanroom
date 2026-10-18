# A-97 (Q-91): T10R108 R-zone geometry — DERIVED

Bed: census cells N=55109..55364 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P110-M re-derived
byte-exact from 55045..55060 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig b3000000. 17th 100B zone.
  NO head singletons.
- m-tab EXACTLY pos[6,7,76,77,78,79], q-indep 256/256,
  16/16 distinct. q-tab EXACTLY pos[50,51,72,73,74,75],
  m-indep 256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (50th)
- R108-q[i] == P110-M[i] full 6B all 16 (heads b50,51 IN
  PLACE; tails 76..79 -> 72..75). Zero breaks.

## 3. b5 rule + dips: NONE (const-count CORRECT)
- b4=(0x8b+2off)&FF 256/256; b5=0xae+(off>=59)+
  (off>=187) 256/256 (dbl-carry). Edges 55167->55168,
  55295->55296 as writer observed.
- varpos EXACTLY tabs+{4,5} (14 var), 70 consts
  first-hand — writer "68 consts" CORRECTED. 0
  stragglers. NO D-class dips.

## geometry agrees on all 3 legs
