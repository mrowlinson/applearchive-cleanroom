# A-101 (Q-95): T10R110 R-zone geometry — DERIVED

Bed: census N=55805..56060 own bed (.rav[12:-4]).
First-hand this shift; P112-M re-derived 55741 row0.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c7000000 NEW. 19th
  100B zone. NO head singletons.
- m-tab EXACTLY pos[32,33,38,39,76,77,78,79] indep
  256/256, 16/16 distinct (b38,39 13 distinct;
  b32,33 2-val: 70e4 m<4 / 10e8 m>=4).
- q-tab EXACTLY pos[44,45,46,72,73,74,75] indep
  256/256, 16/16 distinct (b44-46 15, q13==q14
  head ad7c55). 0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (52nd, 1st m-carried)
- R110-M tails b76..79 == P112 quad-M tails all 16,
  zero breaks. q-tab ALL NEW (0/16 head/tail in
  P112-M set).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xfb+2off)&FF 256/256; b5=0xb3+(off>=3)+
  (off>=131) 256/256 dbl-carry. Edges 55807->55808,
  55935->55936 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
