# A-83 (Q-77): T10R101 single-zone geometry — DERIVED

Bed: census cells N=52673..52928 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P103-M rows
re-derived byte-exact from 52609..52672 quad.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 04000000 (first-hand set
  size 1). 10th 100B zone. NO head singletons.
- m-tab EXACTLY pos[11,19,25,26,27,72,73,74,75] (1st 9B
  m-tab), q-indep 256/256, 16/16 distinct.
- q-tab EXACTLY pos[20,21,76,77,78,79], m-indep 256/256,
  16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (43rd instance)
- R101-q[i] == P103-M[i] full 6B all 16 (heads relocated
  16,17 -> 20,21; tails relocated 72..75 -> 76..79).
  Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0x83+2off)&FF 256/256; b5=0x9b+(off>=63)+
  (off>=191) 256/256 (dbl-carry).
- Edges as writer observed: 52735 255/155 -> 52736 1/156;
  52863 255/156 -> 52864 1/157 (b5 set {155,156,157}).
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
