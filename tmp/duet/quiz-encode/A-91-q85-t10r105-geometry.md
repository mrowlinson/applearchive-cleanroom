# A-91 (Q-85): T10R105 R-zone geometry — DERIVED

Bed: census cells N=54065..54320 on disk (own bed, payload
.rav[12:-4]). First-hand this shift; P107-M re-derived
byte-exact from 54001..54016 quad row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 5b000000 (NEW). 14th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[44,45,50,51,76,77,78,79], q-indep
  256/256, 16/16 distinct. q-tab EXACTLY pos[34,42,43,
  72,73,74,75], m-indep 256/256, 16/16 distinct.

## 2. arithmetic reuse 16/16: CONFIRM (1st non-verbatim)
- tails b72..75 == P107-M tails verbatim 16/16.
- heads R105 b42,43 = LE-u16(P107-M b44,45) x2 mod 2^16,
  16/16 zero breaks (carry pattern fits).
- R105 b34 = P107-M b46 >> 1, 16/16 (2-pt step fit also
  holds; arithmetic reading stands as writer framed).

## 3. b5 rule + dips: NONE
- b4=(0x63+2off)&FF 256/256; b5=0xa6+(off>=79)+
  (off>=207) 256/256 (dbl-carry). Edges 54143->54144,
  54271->54272 as writer observed.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
