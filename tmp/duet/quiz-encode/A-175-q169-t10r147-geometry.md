# A-175 (Q-169): T10R147 R-zone geometry — DERIVED

Bed: census N=68681..68936 own bed (.rav[12:-4]).
First-hand; P149-M from own P149 census row0
68617..68632 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c1240300 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[21,31,38,39,76,77,78,
  79] q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (89th)
- R147-q[i] == P149-M[i] full 7B all 16,
  zero breaks (q-carried, heads b32,33,34
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P149-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x93+2off)&FF 256/256; b5=0x18+
  (off>=55)+(off>=183) 256/256 (dbl-carry).
  Edges 68735->68736 ff/18->01/19, 68863->
  68864 ff/19->01/1a as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
