# A-189 (Q-183): T10R153 R-zone geometry — DERIVED

Bed: census N=70769..71024 own bed (.rav[12:-4]).
First-hand; P155-M from own P155 census row0
70705..70720 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig acaf0300 NEW.
  NO head singletons.
- m-tab 8B EXACTLY pos[44,45,50,51,72,73,74,
  75] q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 7B EXACTLY pos[34,42,43,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (95th)
- R153-q tails 76..79 == P155-M tails 76..79
  full 4B all 16, zero breaks, IN PLACE
  (q-carried tail-only, 12th).
- Heads b34,42,43 novel: 0/16 vs P155M heads
  (15/16 distinct triples).
- m-tails 0/16 vs P155-M (16/16 distinct):
  CONFIRM under m-tab-tail reading (m-tab tail
  part 72..75; 76..79 here is q-tab, const
  across m — same note as A-186).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xe3+2off)&FF 256/256; b5=0x28+
  (off>=15)+(off>=143) 256/256 (dbl-carry).
  Edges 70783->70784 ff/28->01/29, 70911->
  70912 ff/29->01/2a as writer.
- varpos EXACTLY tabs+{4,5}, 67 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
