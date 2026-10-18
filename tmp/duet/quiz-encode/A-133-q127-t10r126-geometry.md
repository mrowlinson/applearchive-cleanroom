# A-133 (Q-127): T10R126 R-zone geometry — DERIVED

Bed: census N=61373..61628 own bed (.rav[12:-4]).
First-hand; P128-M re-derived 61309 row0 (A-132
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c2080000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[44,45,46,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 6B EXACTLY pos[32,38,39,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM, 1 head CORRECT (68th)
- R126-q tails 76..79 == P128-M tails full 4B
  all 16, zero breaks, IN PLACE (q-carried
  tail-only, 4th after R113/R118/R121).
- Heads b32,38,39: 15/16 distinct triples as
  writer -- BUT q-b39 overlaps P128M-b39 1/16
  (qi0 = 0xbe, in P128M-b39 set), NOT 0/16.
  Tail carry itself unaffected (tails 16/16).
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x7b+2off)&FF 256/256; b5=0xdf+
  (off>=67)+(off>=195) 256/256 (dbl-carry).
  Edges 61439->61440 ff/df->01/e0, 61567->
  61568 ff/e0->01/e1 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## legs 1+3 agree; leg2 CONFIRMS carry, CORRECTS b39 0/16->1/16
