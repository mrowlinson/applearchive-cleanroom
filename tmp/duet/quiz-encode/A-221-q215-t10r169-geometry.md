# A-221 (Q-215): T10R169 R-zone geometry — DERIVED

Bed: census N=76337..76592 own bed (.rav[12:-4]).
First-hand; P171-M row0/row3 from own P171
census 76273..76288/76321..76336 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 1c1d4a00 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[44,50,51,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails relocated 76..79 -> 72..75, 2nd;
  m-tab carries no 76..79).
- q-tab 9B EXACTLY pos[23,34,35,42,43,76,77,
  78,79] m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse ROW0-FRAME 16/16: CONFIRM (111th)
- R169-q[i] == P171-M[i] ROW0-FRAME full 9B
  all 16, zero breaks (FULLY IN PLACE incl
  b42 row0 value; row0 carry is 1st).
- Row3-frame 0/16 full (b42 row3-flip 0/16
  positional). Non-42 bytes 16/16 either
  frame x2.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x63+2off)&FF 256/256; b5=0x54+
  (off>=79)+(off>=207) 256/256 (dbl-carry).
  Edges 76415->76416 ff/54->01/55, 76543->
  76544 ff/55->01/56 as writer.
- varpos EXACTLY tabs+{4,5}, 66 consts,
  0 stragglers. NO D-class dips.
- Next tier @76593: PB0 4b000000, PB1 56640000
  (== P171-PBB sig, 1st PB1-echoes-prior-PBB).

## geometry agrees on all 3 legs
