# A-155 (Q-149): T10R137 R-zone geometry — DERIVED

Bed: census N=65201..65456 own bed (.rav[12:-4]).
First-hand; P139-M re-derived 65137 row0 (A-154
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 66ca0000 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[44,45,50,51,76,77,78,
  79] (ties widest) q-indep 256/256, tuple
  16/16 distinct, ALL NEW (m-tails 0/16 vs
  prior-R m-tails).
- q-tab 7B EXACTLY pos[34,42,43,72,73,74,75]
  m-indep 256/256, tuple 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (79th)
- R137-q tails 72..75 == P139-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 7th).
- Heads b34,42,43 novel (15/16 distinct
  triples).
- m-tails 0/16 vs P139-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x63+2off)&FF 256/256; b5=0xfd+
  (off>=79)+(off>=207) 256/256 (dbl-carry).
  Edges 65279->65280 ff/fd->01/fe, 65407->
  65408 ff/fe->01/ff as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
