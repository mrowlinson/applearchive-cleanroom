# A-143 (Q-137): T10R131 R-zone geometry — DERIVED

Bed: census N=63113..63368 own bed (.rav[12:-4]).
First-hand; P133-M re-derived 63049 row0 (A-142
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 07140000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[38,39,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 8B EXACTLY pos[32,33,34,35,72,73,74,
  75] m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (73rd)
- R131-q[i] == P133-M[i] full 8B all 16 (heads
  b32,33,34,35 IN PLACE; tails relocated 76..79
  -> 72..75). Zero breaks, q-carried.
- m-tails 0/16 vs P133-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x13+2off)&FF 256/256; b5=0xed+
  (off>=119)+(off>=247) 256/256 (dbl-carry).
  Edges 63231->63232 ff/ed->01/ee, 63359->
  63360 ff/ee->01/ef as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
