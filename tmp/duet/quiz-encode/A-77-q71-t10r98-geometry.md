# A-77 (Q-71): T10R98 single-zone geometry — DERIVED

Bed: census cells N=51629..51884 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P100-M rows
re-derived byte-exact from 51565..51628 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 02000000 (NEW sig,
  first-hand set size 1). 7th 100B zone. NO head singletons.
- m-tab EXACTLY pos[22,23,76,77,78,79], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[8,9,10,72,73,74,75], m-indep 256/256,
  16/16 distinct.

## 2. tail-4 reuse 16/16 same-pos: CONFIRM (40th instance)
- R98-q[i][72..75] == P100-M[i][72..75] all 16 AT SAME
  positions. Zero breaks.
- q-heads b8,9,10 NEW (0/16 overlap w/ P100-M heads).

## 3. b5 rule + dips: NONE
- b4=(0x5b+2off)&FF 256/256; b5=0x93+(off>=83)+
  (off>=211) 256/256 (dbl-carry).
- Edges as writer observed: 51711 255/147 -> 51712 1/148;
  51839 255/148 -> 51840 1/149 (b5 set {147,148,149}).
- varpos EXACTLY tabs+{4,5}, 69 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
