# A-105 (Q-99): T10R112 R-zone geometry — DERIVED

Bed: census N=56501..56756 own bed (.rav[12:-4]).
First-hand; P114-M re-derived 56437 row0 (A-104).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig cf000000 NEW. 21st
  100B zone. NO head singletons.
- m-tab 6B EXACTLY pos[32,33,76,77,78,79] indep
  256/256, 16/16 distinct (b32,33 alone 14: pairs
  m10==m11 b1fc, m12==m13 b5fc first-hand).
- q-tab 8B EXACTLY pos[18,19,26,27,72,73,74,75]
  indep 256/256, 16/16 distinct (heads alone 13).
  0 violations.

## 2. verbatim reuse 16/16: CONFIRM (54th, q-carried returns) + STRENGTHEN
- Writer tails claim holds; STRONGER first-hand:
  R112-Q FULL 8B == P114 quad-M 8B all 16, zero
  breaks (heads b18,19,26,27 IN PLACE; tails
  76..79 -> 72..75).
- m-tab ALL NEW (0/16 head/tail in P114-M set).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x6b+2off)&FF 256/256; b5=0xb9+(off>=75)+
  (off>=203) 256/256. Edges 56575->56576,
  56703->56704 as writer.
- varpos EXACTLY tabs+{4,5}, 68 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
