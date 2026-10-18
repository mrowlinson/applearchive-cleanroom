# A-73 (Q-67): T10R96 single-zone geometry — DERIVED

Bed: census cells N=50933..51188 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P98-M rows
re-derived byte-exact from 50869..50932 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 5th 100B zone. NO head singletons.
- m-tab EXACTLY pos[28,33,34,35,76,77,78,79], q-indep
  256/256, 16/16 distinct.
- q-tab EXACTLY pos[18,19,26,27,72,73,74,75], m-indep
  256/256, 16/16 distinct.

## 2. tail-4 reuse 16/16 same-pos: CONFIRM (38th instance)
- R96-q[i][72..75] == P98-M[i][72..75] all 16 AT SAME
  positions. Zero breaks.
- q-heads b18,19,26,27 NEW (0/16 overlap w/ P98-M heads).

## 3. b5 rule + dips: NONE
- b4=(0xeb+2off)&FF 256/256; b5=0x8d+(off>=11)+
  (off>=139) 256/256 (dbl-carry).
- Edges as writer observed: 50943 255/141 -> 50944 1/142;
  51071 255/142 -> 51072 1/143 (b5 set {141,142,143}).
- varpos EXACTLY tabs+{4,5}, 66 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
