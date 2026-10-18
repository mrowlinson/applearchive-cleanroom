# A-186 (Q-180): T10R152 R-zone geometry — DERIVED

Bed: census N=70421..70676 own bed (.rav[12:-4]).
First-hand; P154-M from own P154 census row0
70357..70372 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 94890300 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 6B EXACTLY pos[26,27,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (94th)
- R152-q tails 76..79 == P154-M tails 76..79
  full 4B all 16, zero breaks, IN PLACE
  (q-carried tail-only, 11th).
- Heads b26,27 novel: 0/16 vs P154M heads
  (also 0/16 vs P154M (b26,27)-projection,
  0/16 positional; 14/16 distinct pairs).
- m-tails 0/16 vs P154-M (16/16 distinct):
  CONFIRM under m-tab-tail reading (m-tab
  tail part 72..75, 16/16 distinct, 0/16
  overlap). Note: 76..79 here is q-tab
  (const across m), so a 76..79@mcells
  reading is degenerate (16/16 overlap,
  distinct 1 = carried q=0 tails).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x2b+2off)&FF 256/256; b5=0x26+
  (off>=107)+(off>=235) 256/256 (dbl-carry).
  Edges 70527->70528 ff/26->01/27, 70655->
  70656 ff/27->01/28 as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
