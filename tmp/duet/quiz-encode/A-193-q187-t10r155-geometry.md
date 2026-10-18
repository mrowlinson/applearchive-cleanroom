# A-193 (Q-187): T10R155 R-zone geometry — DERIVED

Bed: census N=71465..71720 own bed (.rav[12:-4]).
First-hand; P157-M from own P157 census row0
71401..71416 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig c4050700 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[38,39,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (97th)
- R155-q[i] == P157-M[i] full 7B all 16,
  zero breaks (q-carried, heads b32,33,34
  IN PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P157-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x53+2off)&FF 256/256; b5=0x2e+
  (off>=87)+(off>=215) 256/256 (dbl-carry).
  Edges 71551->71552 ff/2e->01/2f, 71679->
  71680 ff/2f->01/30 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
