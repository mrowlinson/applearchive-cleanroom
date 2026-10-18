# A-165 (Q-159): T10R142 R-zone geometry — DERIVED

Bed: census N=66941..67196 own bed (.rav[12:-4]).
First-hand; P144-M from own P144 census row0
66877..66892 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig aaa90100 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[44,45,46,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 8B EXACTLY pos[32,33,38,39,72,73,
  74,75] m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (84th)
- R142-q[i] == P144-M[i] full 8B all 16,
  zero breaks (q-carried, heads b32,33,38,39
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P144-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xfb+2off)&FF 256/256; b5=0x0a+
  (off>=3)+(off>=131) 256/256 (dbl-carry).
  Edges 66943->66944 ff/0a->01/0b, 67071->
  67072 ff/0b->01/0c as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
