# A-153 (Q-147): T10R136 R-zone geometry — DERIVED

Bed: census N=64853..65108 own bed (.rav[12:-4]).
First-hand; P138-M re-derived 64789 row0 (A-152
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig fbb30000 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 9B EXACTLY pos[20,21,25,26,27,76,77,
  78,79] (ties widest) m-indep 256/256, tuple
  16/16 distinct. 0 violations.

## 2. tail carry 16/16 positional: CONFIRM (78th)
- R136-q tails 76..79 == P138-M tails full 4B
  all 16, zero breaks, IN PLACE (q-carried
  tail-only, 6th).
- Heads b20,21,25,26,27 ALL novel: q-b27 0/16
  vs P138M-b27; b20,21,25,26 15/16 distinct
  quads (full-head 15/16).
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xab+2off)&FF 256/256; b5=0xfa+
  (off>=43)+(off>=171) 256/256 (dbl-carry).
  Edges 64895->64896 ff/fa->01/fb, 65023->
  65024 ff/fb->01/fc as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
