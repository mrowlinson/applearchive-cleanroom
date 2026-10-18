# A-119 (Q-113): T10R119 R-zone geometry — DERIVED

Bed: census N=58937..59192 own bed (.rav[12:-4]).
First-hand; P121-M re-derived 58873 row0 (A-118
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 25020000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[13,14,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 6B EXACTLY pos[6,7,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (61st)
- R119-q[i] == P121-M[i] full 6B all 16 (heads
  b6,7 AND tails 76..79 IN PLACE, no relocation
  -- 1st no-relocation verbatim). Zero breaks.
- q-carried, byte-exact (not arithmetic).
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x73+2off)&FF 256/256; b5=0xcc+
  (off>=71)+(off>=199) 256/256 (dbl-carry).
  Edges 59007->59008 ff/cc->01/cd, 59135->
  59136 ff/cd->01/ce as writer.
- varpos EXACTLY tabs+{4,5}, 70 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
