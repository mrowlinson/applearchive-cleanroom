# A-107 (Q-101): T10R113 R-zone geometry — DERIVED

Bed: census N=56849..57104 own bed (.rav[12:-4]).
First-hand; P115-M re-derived 56785 row0 (A-106).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 8a000000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[44,45,50,51,76,77,78,79]
  indep 256/256, 16/16 distinct. q-tab 8B EXACTLY
  pos[33,34,42,43,72,73,74,75] indep 256/256,
  16/16 distinct. 0 violations.

## 2. reuse vs P115-M: VERBATIM q-tails (55th, q-carried)
- R113-Q tails b72..75 == P115 quad-M b76..79
  row0 all 16, zero breaks (56785..56800 derived).
  NOT arithmetic, NOT novel (byte-diffs all 0).
- q heads b33,34,42,43 ALL NEW; m-tab ALL NEW
  (tails 0/16 positional, byte-diffs scattered
  16-val/byte = no const-offset arithmetic).
- Carry sequence now: R110 m, R111 m, R112 q,
  R113 q.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x23+2off)&FF 256/256; b5=0xbc+(off>=111)+
  (off>=239) 256/256. Edges 56959->56960,
  57087->57088 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
