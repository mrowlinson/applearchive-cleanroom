# A-259 (Q-253): T10R188 R-zone geometry — DERIVED

Bed: census N=82949..83204 own bed (.rav[12:-4]). First-hand; P190-M from own P190
census row0 82885..82900 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 17e63403 NEW. NO head singletons.
- CLASSIC: m-tab 6B EXACTLY pos[6,7,76,77,78,79] q-indep 256/256, 16/16
  distinct, ALL NEW (m-tails 0/16 vs P190M; IN PLACE).
- q-tab 7B EXACTLY pos[48,49,50,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-7B (130th)
- R188-q[i] == P190-M[i] full 7B all 16, zero breaks (heads b48-50 IN PLACE,
  tails relocated 76..79->72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x0b+2off)&FF 256/256; b5=0x88+(off>=123)+(off>=251) 256/256 (dbl-carry).
- Edges 83071->83072 ff/88->01/89, 83199->83200 ff/89->01/8a as writer.
- varpos EXACTLY tabs+{4,5} (15), 69 consts, 0 stragglers. NO D-class dips.
- Next tier @83205: PB0 1e030000 (repeat x3 of P189/P190 PB0), PB1 6a410600,
  PBA 83207..83208 sig d2166400 — all 3 as writer.

## geometry agrees on all 3 legs
