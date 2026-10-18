# A-135 (Q-129): T10R127 R-zone geometry — DERIVED

Bed: census N=61721..61976 own bed (.rav[12:-4]).
First-hand; P129-M re-derived 61657 row0 (A-134
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 55050000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 6B EXACTLY pos[6,7,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (69th)
- R127-q[i] == P129-M[i] full 6B all 16 (heads
  b6,7 AND tails 76..79 IN PLACE, no relocation
  -- 2nd no-relocation verbatim after R119).
  Zero breaks, q-carried.
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x33+2off)&FF 256/256; b5=0xe2+
  (off>=103)+(off>=231) 256/256 (dbl-carry).
  Edges 61823->61824 ff/e2->01/e3, 61951->
  61952 ff/e3->01/e4 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
