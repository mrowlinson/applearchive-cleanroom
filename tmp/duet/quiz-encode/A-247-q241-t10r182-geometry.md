# A-247 (Q-241): T10R182 R-zone geometry — DERIVED

Bed: census N=80861..81116 own bed (.rav[12:-4]). First-hand; P184-M from own P184
census row0 80797..80812 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 9f34d402 NEW. NO head singletons.
- CLASSIC: m-tab 8B EXACTLY pos[23,35,42,43,76,77,78,79] q-indep 256/256,
  16/16 distinct, ALL NEW (m-tails 0/16 vs P184M; IN PLACE).
- q-tab 6B EXACTLY pos[36,37,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-6B (124th)
- R182-q[i] == P184-M[i] full 6B all 16, zero breaks: heads b36,37 IN PLACE
  16/16 positional, tails relocated 76..79->72..75 16/16 positional.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xbb+2off)&FF 256/256; b5=0x77+(off>=35)+(off>=163) 256/256 (dbl-carry).
- Edges 80895->80896 ff/77->01/78, 81023->81024 ff/78->01/79 as writer.
- varpos EXACTLY tabs+{4,5} (16), 68 consts, 0 stragglers. NO D-class dips.
- Next tier @81117: PB0 d0020000 (repeat of P184 PB0), PB1 9b540200,
  PBA 81119..81120 sig 9f342c00 (== P184 QUAD sig, own bed) — all 3 as writer.

## geometry agrees on all 3 legs
