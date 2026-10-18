# A-169 (Q-163): T10R144 R-zone geometry — DERIVED

Bed: census N=67637..67892 own bed (.rav[12:-4]).
First-hand; P146-M tails from own P146 census
row0 67573..67588 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 04050100 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (72..75 layout, no 76..79).
- q-tab 8B EXACTLY pos[20,25,26,27,76,77,78,
  79] m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (86th)
- R144-q tails 76..79 == P146-M tails full 4B
  all 16, zero breaks, IN PLACE (q-carried
  tail-only, 8th).
- Heads b20,25,26,27 novel (15/16 distinct
  quads). m-tab carries no 76..79 (72..75
  instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x6b+2off)&FF 256/256; b5=0x10+
  (off>=75)+(off>=203) 256/256 (dbl-carry).
  Edges 67711->67712 ff/10->01/11, 67839->
  67840 ff/11->01/12 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
