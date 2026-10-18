# A-67 (Q-61): T10R93 single-zone geometry — DERIVED

Bed: census cells N=49889..50144 on disk (own bed, payload
.rav[12:-4]). All 84B. First-hand this shift; P95-M rows
re-derived byte-exact from 49825..49888.
(ACK PARENT-042: Q-61 missed in hb1104 poll gap — answered
now, polling every turn.)

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 01000000 (first-hand set
  size 1). 2nd 100B zone. NO head singletons.
- m-tab EXACTLY pos[28,29,30,72,73,74,75], q-indep 256/256,
  16/16 distinct.
- q-tab EXACTLY pos[20,21,22,76,77,78,79], m-indep 256/256,
  16/16 distinct.

## 2. tail-4 reuse 16/16 positional: CONFIRM (35th instance)
- R93-q[i][76..79] == P95-M[i][72..75] all 16 (tails
  relocated 72..75 -> 76..79). Zero breaks.
- q-prefix split EXACT: b21=df/b22=02 q0-8, b21=5a/
  b22=03 q9-15; b20 varies.

## 3. b5 rule + dips: NONE
- b4=(0xc3+2off)&FF 256/256; b5=0x85+(off>=31)+
  (off>=159) 256/256 (dbl-carry).
- Edges as writer observed: 49919 255/133 -> 49920 1/134;
  50047 255/134 -> 50048 1/135 (b5 set {133,134,135}).
- varpos EXACTLY tabs+{4,5}, 68 consts, 0 stragglers;
  0 tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 3 legs
