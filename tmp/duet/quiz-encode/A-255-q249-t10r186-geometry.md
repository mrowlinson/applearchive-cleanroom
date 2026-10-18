# A-255 (Q-249): T10R186 R-zone geometry — DERIVED

Bed: census N=82253..82508 own bed (.rav[12:-4]). First-hand; P188-M from own P188
census row0 82189..82204 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig aafe1e03 NEW. NO head singletons.
- TAILS-SWAP cont: m-tab 7B EXACTLY pos[20,21,22,72,73,74,75] q-indep 256/256,
  16/16 distinct, ALL NEW (m-tails 0/16 vs P188M; RELOCATED 76..79->72..75).
- q-tab 6B EXACTLY pos[13,15,76,77,78,79] m-indep 256/256, 16/16 distinct
  (tails IN PLACE). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-6B (128th)
- R186-q[i] == P188-M[i] full 6B all 16, zero breaks (heads b13,15 IN PLACE,
  tails b76-79 IN PLACE).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x9b+2off)&FF 256/256; b5=0x82+(off>=51)+(off>=179) 256/256 (dbl-carry).
- Edges 82303->82304 ff/82->01/83, 82431->82432 ff/83->01/84 as writer.
- varpos EXACTLY tabs+{4,5} (15), 69 consts, 0 stragglers. NO D-class dips.
- Next tier @82509: PB0 1e030000 (NEW PB0 sig), PB1 fe1e0300,
  PBA 82511..82512 sig 99573100 — all 3 as writer.

## geometry agrees on all 3 legs
