# A-251 (Q-245): T10R184 R-zone geometry — DERIVED

Bed: census N=81557..81812 own bed (.rav[12:-4]). First-hand; P186-M from own P186
census row0 81493..81508 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig f51af502 NEW. NO head singletons.
- CLASSIC: m-tab 7B EXACTLY pos[32,33,34,76,77,78,79] q-indep 256/256, 16/16
  distinct, ALL NEW (m-tails 0/16 vs P186M; IN PLACE).
- q-tab 7B EXACTLY pos[24,25,26,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. partial reuse: CONFIRM (tails-only, R171-style, 126th)
- q-tails == P186-M tails 16/16 POSITIONAL (relocated).
- q-b24,25,26 novel POSITIONALLY: 0/16 vs EACH P186M head b20,21,26,27
  (all 12 position pairs 0). Set collisions 2/16, 7/16, 0/16 EXACTLY as
  writer — chance, no positional breaks. 4/7 bytes verbatim.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x2b+2off)&FF 256/256; b5=0x7d+(off>=107)+(off>=235) 256/256 (dbl-carry).
- Edges 81663->81664 ff/7d->01/7e, 81791->81792 ff/7e->01/7f as writer.
- varpos EXACTLY tabs+{4,5} (16), 68 consts, 0 stragglers. NO D-class dips.
- Next tier @81813: PB0 f6020000 (repeat of P186 PB0), PB1 3b070500,
  PBA 81815..81816 sig 3b075d00 — all 3 as writer.

## geometry agrees on all 3 legs
