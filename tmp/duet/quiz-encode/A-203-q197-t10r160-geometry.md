# A-203 (Q-197): T10R160 R-zone geometry — DERIVED

Bed: census N=73205..73460 own bed (.rav[12:-4]).
First-hand; P162-M tails from own P162 census
row0 73141..73156 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 1c2d0800 NEW.
  NO head singletons.
- m-tab 7B EXACTLY pos[32,33,34,72,73,74,75]
  q-indep 256/256, 16/16 distinct, ALL NEW.
- q-tab 6B EXACTLY pos[26,27,76,77,78,79]
  m-indep 256/256, 16/16 distinct.
  0 violations.

## 2. tail carry 16/16 positional: CONFIRM (102nd)
- R160-q tails 76..79 == P162-M tails 76..79
  full 4B all 16, zero breaks, IN PLACE
  (q-carried tail-only, 14th).
- Heads b26,27 novel: 0/16 positional vs
  EVERY P162 row x4 (14/16 distinct pairs);
  b26 alone 0/16 positional vs all 4
  XOR-split rows x4.
- m-tails 0/16 vs P162-M (16/16 distinct):
  CONFIRM under m-tab-tail reading (m-tab
  tail part 72..75; same note as A-186).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xeb+2off)&FF 256/256; b5=0x3b+
  (off>=11)+(off>=139) 256/256 (dbl-carry).
  Edges 73215->73216 ff/3b->01/3c, 73343->
  73344 ff/3c->01/3d as writer.
- varpos EXACTLY tabs+{4,5}, 69 consts,
  0 stragglers. NO D-class dips.

## geometry agrees on all 3 legs
