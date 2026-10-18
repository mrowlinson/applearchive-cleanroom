# A-181 (Q-175): T10R150 R-zone geometry — DERIVED

Bed: census N=69725..69980 own bed (.rav[12:-4]).
First-hand; P152-M tails from own P152 census
row0 69661..69676 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 2dbd0300 NEW.
  NO head singletons.
- m-tab 5B EXACTLY pos[44,76,77,78,79]
  (ties smallest m-tab) q-indep 256/256,
  16/16 distinct, ALL NEW.
- q-tab 6B EXACTLY pos[36,37,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (92nd)
- R150-q tails 72..75 == P152-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 10th).
- Heads b36,37 novel (14/16 distinct pairs).
  m-tails 0/16 vs P152-M tails (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xbb+2off)&FF 256/256; b5=0x20+
  (off>=35)+(off>=163) 256/256 (dbl-carry).
  Edges 69759->69760 ff/20->01/21, 69887->
  69888 ff/21->01/22 as writer.
- varpos EXACTLY tabs+{4,5}, 71 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
