# A-123 (Q-117): T10R121 R-zone geometry — DERIVED

Bed: census N=59633..59888 own bed (.rav[12:-4]).
First-hand; P123-M re-derived 59569 row0 (A-122
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 92010000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[44,45,50,51,76,77,78,
  79] q-indep 256/256, tuple 16/16 distinct,
  ALL NEW (b44,45 const 8cb3 except m15 =
  4cb4; m-tails 0/16 vs prior-R m-tails).
- q-tab 8B EXACTLY pos[33,34,42,43,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (63rd)
- R121-q tails 72..75 == P123-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 3rd
  after R113/R118).
- Heads b33,34,42,43 novel (14/16 distinct).
- m-tab 0/16 vs P123-M on shared6 b44,45,
  76..79.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xe3+2off)&FF 256/256; b5=0xd1+
  (off>=15)+(off>=143) 256/256 (dbl-carry).
  Edges 59647->59648 ff/d1->01/d2, 59775->
  59776 ff/d2->01/d3 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
