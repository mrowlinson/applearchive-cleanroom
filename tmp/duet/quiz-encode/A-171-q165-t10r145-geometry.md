# A-171 (Q-165): T10R145 R-zone geometry — DERIVED

Bed: census N=67985..68240 own bed (.rav[12:-4]).
First-hand; P147-M tails from own P147 census
row0 67921..67936 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 89300300 NEW.
  NO head singletons.
- m-tab 9B EXACTLY pos[44,45,46,50,51,76,77,
  78,79] (widest m-tab) q-indep 256/256,
  16/16 distinct, ALL NEW.
- q-tab 8B EXACTLY pos[34,35,42,43,72,73,74,
  75] m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (87th)
- R145-q tails 72..75 == P147-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 9th).
- Heads b34,35,42,43 novel (15/16 distinct
  quads). m-tails 0/16 vs P147-M tails.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x23+2off)&FF 256/256; b5=0x13+
  (off>=111)+(off>=239) 256/256 (dbl-carry).
  Edges 68095->68096 ff/13->01/14, 68223->
  68224 ff/14->01/15 as writer.
- varpos EXACTLY tabs+{4,5}, 65 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
