# A-63 (Q-57): T10R91 single-zone geometry — DERIVED

Bed: census cells N=49193..49448 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift; P93-QM rows
re-derived byte-exact from 49129..49192.

## 1. single 16x16 zone: CONFIRM
- 256/256 96B/80B, single sig 38fcd5d1 (first-hand set
  size 1). NO head singletons.
- m-tab EXACTLY pos[34,35,72,73,74,75], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[28,30,31,68,69,70,71], m-indep
  256/256, 16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (33rd instance)
- R91-q[i] == P93-QM[i] full 7B byte-for-byte all 16
  (P93M re-derived first-hand from 49129..49192 4x16,
  16/16 distinct; tails relocated 72..75 -> 68..71).
  Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x53+2off)&FF 256/256; b5=0x80+(off>=87)+
  (off>=215) 256/256 (dbl-carry).
- Edges as writer observed: 49279 255/128 -> 49280 1/129;
  49407 255/129 -> 49408 1/130 (b5 set {128,129,130}).
- varpos EXACTLY tabs+{4,5}, 65 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
