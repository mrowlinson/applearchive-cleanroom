# A-167 (Q-161): T10R143 R-zone geometry — DERIVED

Bed: census N=67289..67544 own bed (.rav[12:-4]).
First-hand; P145-M from own P145 census row0
67225..67240 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig d3770200 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[13,14,15,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (72..75 layout, no 76..79).
- q-tab 6B EXACTLY pos[6,7,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (85th)
- R143-q[i] == P145-M[i] full 6B all 16,
  zero breaks, q-carried (heads b6,7 AND
  tails 76..79 IN PLACE, no relocation --
  4th no-relocation verbatim).
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xb3+2off)&FF 256/256; b5=0x0d+
  (off>=39)+(off>=167) 256/256 (dbl-carry).
  Edges 67327->67328 ff/0d->01/0e, 67455->
  67456 ff/0e->01/0f as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
