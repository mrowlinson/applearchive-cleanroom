# A-199 (Q-193): T10R158 R-zone geometry — DERIVED

Bed: census N=72509..72764 own bed (.rav[12:-4]).
First-hand; P160-M tails from own P160 census
row0 72445..72460 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 7ab40700 NEW.
  NO head singletons.
- m-tab 6B EXACTLY pos[44,45,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 7B EXACTLY pos[36,37,38,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (100th)
- R158-q tails 72..75 == P160-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 13th).
- Heads b36,37,38 novel: 0/16 vs P160M heads
  b33,38,39 (15/16 distinct triples); b38
  alone 0/16 positional.
- m-tails 0/16 vs P160-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x7b+2off)&FF 256/256; b5=0x36+
  (off>=67)+(off>=195) 256/256 (dbl-carry).
  Edges 72575->72576 ff/36->01/37, 72703->
  72704 ff/37->01/38 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
