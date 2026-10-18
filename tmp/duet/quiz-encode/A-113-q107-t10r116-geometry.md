# A-113 (Q-107): T10R116 R-zone geometry — DERIVED

Bed: census N=57893..58148 own bed (.rav[12:-4]).
First-hand; P118-M re-derived 57829 row0 (A-112
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig ba010000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[6,7,76,77,78,79]
  q-indep 256/256 (16 m per q), 16/16
  distinct, ALL NEW.
- q-tab 7B EXACTLY pos[44,50,51,72,73,74,75]
  m-indep 256/256 (16 q per m), 16/16
  distinct. 0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (58th, q-carried)
- R116-q[i] == P118-M[i] full 7B all 16,
  zero breaks (q by row, M by col).
  Heads b44,50,51 IN PLACE; tails relocated
  76..79 -> 72..75.
- NOT arithmetic, NOT novel (byte-diffs all 0).
- m-tails 0/16 vs P118-M tails.
- Carry sequence now: ... R115 q, R116 q.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x4b+2off)&FF 256/256; b5=0xc4+(off>=91)+
  (off>=219) 256/256 (dbl-carry, wrap-driven).
  Edges 57983->57984 ff/c4->01/c5,
  58111->58112 ff/c5->01/c6 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
