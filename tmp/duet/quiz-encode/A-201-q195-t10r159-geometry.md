# A-201 (Q-195): T10R159 R-zone geometry — DERIVED

Bed: census N=72857..73112 own bed (.rav[12:-4]).
First-hand; P161-M from own P161 census row0
72793..72808 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c0d00700 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 8B EXACTLY pos[6,7,8,9,72,73,74,75]
  m-indep 256/256, 16/16 distinct (2nd 8B
  q-tab).
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (101st)
- R159-q[i] == P161-M[i] full 8B all 16,
  zero breaks (q-carried, heads b6-9 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P161-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x33+2off)&FF 256/256; b5=0x39+
  (off>=103)+(off>=231) 256/256 (dbl-carry).
  Edges 72959->72960 ff/39->01/3a, 73087->
  73088 ff/3a->01/3b as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
