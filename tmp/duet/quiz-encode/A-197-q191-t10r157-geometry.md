# A-197 (Q-191): T10R157 R-zone geometry — DERIVED

Bed: census N=72161..72416 own bed (.rav[12:-4]).
First-hand; P159-M from own P159 census row0
72097..72112 (this seat).

## 1. dual-sig 16x16 zone: CONFIRM (2nd dual-sig)
- 256/256 100B/84B: 176x sig 2cd80700 (m0-10
  all rows) + 80x sig 2dd80700 (m11-15 all
  rows), placement exact per-N (1st 11/5
  split). NO head singletons.
- m-tab 9B EXACTLY pos[0,11,19,26,27,76,77,
  78,79] (sig b0 rides in tab: 0x2c m0-10,
  0x2d m11-15) q-indep 256/256, 16/16
  distinct, ALL NEW.
- q-tab 7B EXACTLY pos[20,21,22,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (99th)
- R157-q[i] == P159-M[i] full 7B all 16,
  zero breaks (q-carried, heads b20,21,22
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P159-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xc3+2off)&FF 256/256; b5=0x33+
  (off>=31)+(off>=159) 256/256 (dbl-carry).
  Edges 72191->72192 ff/33->01/34, 72319->
  72320 ff/34->01/35 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
