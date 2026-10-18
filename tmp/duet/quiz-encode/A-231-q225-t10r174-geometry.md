# A-231 (Q-225): T10R174 R-zone geometry — DERIVED

Bed: census N=78077..78332 own bed (.rav[12:-4]). First-hand; P176-M from own P176 census
row0 78013..78028 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig df9a0b01 NEW. NO head singletons.
- m-tab 6B EXACTLY pos[42,43,76,77,78,79] q-indep 256/256, 16/16 distinct,
  ALL NEW (m-tails 0/16 vs P176M; IN PLACE).
- q-tab 6B EXACTLY pos[36,37,72,73,74,75] m-indep 256/256, 16/16 distinct. 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 positional
- R174-q[i] == P176-M[i] full 6B all 16, zero breaks (heads b36,37 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xfb+2off)&FF 256/256; b5=0x61+(off>=3)+(off>=131) 256/256 (dbl-carry).
- Edges per-N exact: 78079->78080 ff/61->01/62; 78207->78208 ff/62->01/63.
- Varpos EXACTLY tabs+{4,5} (14), 70 consts, 0 stragglers. NO D-class dips.
- Next tier @78333: PB0 41010000 (repeat of P176 PB0), PB1 73350100, PBA df9a1700
  (repeat of P176 PBA sig).

## geometry agrees on all 3 legs
