# A-159 (Q-153): T10R139 R-zone geometry — DERIVED

Bed: census N=65897..66152 own bed (.rav[12:-4]).
First-hand; P141-M from own P141 census row0
65833..65848 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 5d190100 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[31,38,39,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (81st)
- R139-q[i] == P141-M[i] full 7B all 16,
  zero breaks (q-carried, heads b32,33,34
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P141-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xd3+2off)&FF 256/256; b5=0x02+
  (off>=23)+(off>=151) 256/256 (dbl-carry).
  Edges 65919->65920 ff/02->01/03, 66047->
  66048 ff/03->01/04 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
