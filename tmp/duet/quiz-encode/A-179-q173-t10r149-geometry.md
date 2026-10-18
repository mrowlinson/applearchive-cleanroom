# A-179 (Q-173): T10R149 R-zone geometry — DERIVED

Bed: census N=69377..69632 own bed (.rav[12:-4]).
First-hand; P151-M from own P151 census row0
69313..69328 (this seat).

## 1. dual-sig 16x16 zone: CONFIRM (1st dual-sig R-zone)
- 256/256 100B/84B: 224x sig 256e0300 (m0-13
  all rows) + 32x sig 266e0300 (m14-15 all
  rows), placement exact per-N. NO head
  singletons.
- m-tab 9B EXACTLY pos[0,11,19,26,27,76,77,
  78,79] (sig b0 rides in tab: 0x25 m0-13,
  0x26 m14,15) q-indep 256/256, 16/16
  distinct, ALL NEW.
- q-tab 6B EXACTLY pos[20,21,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. verbatim reuse 16/16 positional: CONFIRM (91st)
- R149-q[i] == P151-M[i] full 6B all 16,
  zero breaks (q-carried, heads b20,21 IN
  PLACE; tails relocated 76..79 -> 72..75).
- m-tails 0/16 vs P151-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x03+2off)&FF 256/256; b5=0x1e+
  (off>=127)+(off>=255) 256/256 (dbl-carry;
  2nd step at last cell). Edges 69503->69504
  ff/1e->01/1f, 69631->69632 ff/1f->01/20
  as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
