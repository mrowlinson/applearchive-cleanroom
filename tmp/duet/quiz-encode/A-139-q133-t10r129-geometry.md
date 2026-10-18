# A-139 (Q-133): T10R129 R-zone geometry — DERIVED

Bed: census N=62417..62672 own bed (.rav[12:-4]).
First-hand; P131-M re-derived 62353 row0 (A-138
bed, this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig f1090000 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[50,51,76,77,78,79]
  q-indep 256/256, tuple 16/16 distinct, ALL
  NEW (m-tails 0/16 vs prior-R m-tails).
- q-tab 9B EXACTLY pos[33,34,35,42,43,72,73,
  74,75] (widest q-tab) m-indep 256/256, tuple
  16/16 distinct. 0 violations.

## 2. tail carry 16/16 positional: CONFIRM (71st)
- R129-q tails 72..75 == P131-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 5th).
- Heads b33,34,35,42,43 novel (15/16 distinct).
- m-tails 0/16 vs P131-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xa3+2off)&FF 256/256; b5=0xe7+
  (off>=47)+(off>=175) 256/256 (dbl-carry).
  Edges 62463->62464 ff/e7->01/e8, 62591->
  62592 ff/e8->01/e9 as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
