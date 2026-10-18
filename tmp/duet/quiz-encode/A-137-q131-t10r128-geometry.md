# A-137 (Q-131): T10R128 R-zone geometry — DERIVED

Bed: census N=62069..62324 own bed (.rav[12:-4]).
First-hand; P130-M + M26 row-forms re-derived
62005 row0/row2 (A-136 bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 3a090000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[32,33,72,73,74,75]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (72..75 layout, no 76..79).
- q-tab 7B EXACTLY pos[18,26,27,76,77,78,79]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. verbatim + xor-byte 16/16: CONFIRM (70th)
- R128-q shared6 b18,27,76..79 == P130-M full
  6B all 16 IN PLACE, zero breaks.
- q-b26 == P130-M26 row2-form (M26[q]^0x01)
  16/16 (1st xor-byte carry); 0/16 vs row0-form.
- m-tab carries no 76..79 (72..75 instead).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xeb+2off)&FF 256/256; b5=0xe4+
  (off>=11)+(off>=139) 256/256 (dbl-carry).
  Edges 62079->62080 ff/e4->01/e5, 62207->
  62208 ff/e5->01/e6 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
