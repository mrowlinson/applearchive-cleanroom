# A-229 (Q-223): T10R173 R-zone geometry — DERIVED

Bed: census N=77729..77984 own bed (.rav[12:-
4]). First-hand; P175-M from own P175 census
row0 77665..77680 (this seat).

## 1. 16x16 zone, M-VARYING sig: CONFIRM
- 256/256 100B/84B, sig b0 per-m exact =
  96,96,97x11,9dx3 (m0-1 96904101, m2-12
  97904101, m13-15 9d904101; b1 const 0x90;
  counts 32/176/48). NO head singletons.
- m-tab 9B EXACTLY pos[0,11,19,26,27,76,77,
  78,79] q-indep 256/256, 16/16 distinct, ALL
  NEW (m-tails 0/16 vs P175M; IN PLACE).
- q-tab 7B EXACTLY pos[20,21,22,72,73,74,75]
  m-indep 256/256, 16/16 distinct. 0
  violations.

## 2. verbatim reuse: CONFIRM 16/16 positional
- R173-q[i] == P175-M[i] full 7B all 16, zero
  breaks (heads b20-22 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x43+2off)&FF 256/256; b5=0x5f+
  (off>=95)+(off>=223) 256/256 (dbl-carry).
- Edges per-N exact: 77823->77824 ff/5f->
  01/60; 77951->77952 ff/60->01/61.
- Varpos EXACTLY tabs+{4,5} (18), 66 consts,
  0 stragglers. NO D-class dips.
- Next tier @77985: PB0 41010000, PB1
  97410100, PBA df9a1700.

## geometry agrees on all 3 legs
