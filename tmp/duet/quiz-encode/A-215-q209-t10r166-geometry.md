# A-215 (Q-209): T10R166 R-zone geometry — DERIVED

Bed: census N=75293..75548 own bed (.rav[12:-4]).
First-hand; P168-M tails from own P168 census
row0 75229..75244 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 0be43600 NEW
  (b0,b1 == P168-quad sig 0be40200 prefix,
  1st R-sig/P-sig prefix link, per-N exact).
  NO head singletons.
- m-tab 6B EXACTLY pos[42,43,76,77,78,79]
  q-indep 256/256, 16/16 distinct, ALL NEW
  (m-tails IN PLACE).
- q-tab 7B EXACTLY pos[36,37,38,72,73,74,75]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (108th)
- R166-q tails 72..75 == P168-M tails 76..79
  full 4B all 16, zero breaks, relocated
  76..79 -> 72..75 (q-carried tail-only, 15th).
- Heads b36,37,38 novel: 0/16 vs P168M heads
  (13/16 distinct triples); b38 alone 0/16
  positional vs P168M b38.
- m-tails 0/16 vs P168-M (16/16 distinct).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x3b+2off)&FF 256/256; b5=0x4c+
  (off>=99)+(off>=227) 256/256 (dbl-carry).
  Edges 75391->75392 ff/4c->01/4d, 75519->
  75520 ff/4d->01/4e as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
