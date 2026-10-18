# A-249 (Q-243): T10R183 R-zone geometry — DERIVED

Bed: census N=81209..81464 own bed (.rav[12:-4]). First-hand; P185-M from own P185
census row0 81145..81160 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 049b5403 NEW. NO head singletons.
- CLASSIC: m-tab 7B EXACTLY pos[13,14,15,76,77,78,79] q-indep 256/256, 16/16
  distinct, ALL NEW (m-tails 0/16 vs P185M; IN PLACE).
- q-tab 7B EXACTLY pos[6,7,8,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-7B (125th)
- R183-q[i] == P185-M[i] full 7B all 16, zero breaks: heads b6-8 IN PLACE
  16/16 positional, tails relocated 76..79->72..75 16/16 positional.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x73+2off)&FF 256/256; b5=0x7a+(off>=71)+(off>=199) 256/256 (dbl-carry).
- Edges 81279->81280 ff/7a->01/7b, 81407->81408 ff/7b->01/7c as writer.
- varpos EXACTLY tabs+{4,5} (16), 68 consts, 0 stragglers. NO D-class dips.
- Next tier @81465: PB0 f6020000 (NEW PB0 sig), PB1 04f60200,
  PBA 81467..81468 sig 4d602f00 — all 3 as writer.

## geometry agrees on all 3 legs
