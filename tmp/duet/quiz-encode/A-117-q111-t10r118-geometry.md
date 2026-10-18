# A-117 (Q-111): T10R118 R-zone geometry — DERIVED

Bed: census N=58589..58844 own bed (.rav[12:-4]).
First-hand; P120-M re-derived 58525 row0 (A-116
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig e0010000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[44,45,46,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 6B EXACTLY pos[38,39,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (60th)
- R118-q tails 76..79 == P120-M tails 76..79
  full 4B all 16, zero breaks, IN PLACE (no
  72..75 relocation; q-carried tail-only, 2nd
  after R113).
- Heads b38,39 novel: 13/16 distinct pairs;
  b39 3 values 5c/5d/5e only.
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xbb+2off)&FF 256/256; b5=0xc9+
  (off>=35)+(off>=163) 256/256 (dbl-carry).
  Edges 58623->58624 ff/c9->01/ca, 58751->
  58752 ff/ca->01/cb as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
