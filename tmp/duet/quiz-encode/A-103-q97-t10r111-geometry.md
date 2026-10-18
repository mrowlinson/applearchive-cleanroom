# A-103 (Q-97): T10R111 R-zone geometry — DERIVED

Bed: census N=56153..56408 own bed (.rav[12:-4]).
First-hand; P113-M re-derived 56089 row0 (A-102).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig a3000000 NEW. 20th
  100B zone. NO head singletons.
- m-tab EXACTLY pos[6,7,8,76,77,78,79] indep
  256/256, 16/16 distinct (b6-8 alone 15).
- q-tab EXACTLY pos[13,14,15,16,72,73,74,75] indep
  256/256, 16/16 distinct (b13-16 14, b72-75 16).
  0 violations.

## 2. verbatim reuse 16/16: CONFIRM (53rd, m-carried 2nd consec) + STRENGTHEN
- R111-M tails b76..79 == P113 quad-M b76..79 row0
  all 16, zero breaks.
- STRENGTHEN: heads b6,7 ALSO verbatim == P113-M
  b6,7 16/16; 3rd byte coarse-aligned only (R111
  b8 38/b8 vs P113 b12 f9/fd, same 13/3 split @13).
- q-tab ALL NEW (0/16 in P113-M set).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xb3+2off)&FF 256/256; b5=0xb6+(off>=39)+
  (off>=167) 256/256. Edges 56191->56192,
  56319->56320 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
