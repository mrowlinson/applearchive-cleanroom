# A-245 (Q-239): T10R181 R-zone geometry — DERIVED

Bed: census N=80513..80768 own bed (.rav[12:-4]). First-hand; P183-M from own P183
census row0 80449..80464 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 78c4d002 NEW. NO head singletons.
- CLASSIC: m-tab 8B EXACTLY pos[11,19,26,27,76,77,78,79] q-indep 256/256,
  16/16 distinct, ALL NEW (m-tails 0/16 vs P183M; IN PLACE).
- q-tab 7B EXACTLY pos[20,21,22,72,73,74,75] m-indep 256/256, 16/16 distinct
  (tails RELOCATED 76..79->72..75). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-7B (123rd)
- R181-q[i] == P183-M[i] full 7B all 16, zero breaks: heads b20-22 IN PLACE
  16/16 positional, tails relocated 76..79->72..75 16/16 positional.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x03+2off)&FF 256/256; b5=0x75+(off>=127)+(off>=255) 256/256 (dbl-carry).
- Edges 80639->80640 ff/75->01/76, 80767->80768 ff/76->01/77 (2nd edge at
  last cell) as writer.
- varpos EXACTLY tabs+{4,5} (17), 67 consts, 0 stragglers. NO D-class dips.
- Next tier @80769: PB0 d0020000 (NEW PB0 sig), PB1 9f340400,
  PBA 80771..80772 sig 9f345800 — all 3 as writer.

## geometry agrees on all 3 legs
