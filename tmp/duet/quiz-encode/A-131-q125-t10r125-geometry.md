# A-131 (Q-125): T10R125 R-zone geometry — DERIVED

Bed: census N=61025..61280 own bed (.rav[12:-4]).
First-hand; P127-M re-derived 60961 row0 (A-130
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 6f080000 NEW.
  NO head singletons.
- m-tab 5B EXACTLY pos[26,76,77,78,79]
  (smallest m-tab) q-indep 256/256, tuple 16/16
  distinct, ALL NEW (m-tails 0/16 vs prior-R
  m-tails).
- q-tab 8B EXACTLY pos[20,21,22,23,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (67th)
- R125-q[i] == P127-M[i] full 8B all 16 (heads
  b20,21,22,23 IN PLACE; tails relocated 76..79
  -> 72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P127-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xc3+2off)&FF 256/256; b5=0xdc+
  (off>=31)+(off>=159) 256/256 (dbl-carry).
  Edges 61055->61056 ff/dc->01/dd, 61183->
  61184 ff/dd->01/de as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
