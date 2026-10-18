# A-243 (Q-237): T10R180 R-zone geometry — DERIVED

Bed: census N=80165..80420 own bed (.rav[12:-4]). First-hand; P182-M from own P182
census row0 80101..80116 (this seat).

## 1. single zone: CONFIRM
- 256/256 100B/84B exact. Single sig 77f2c402 NEW. NO head singletons.
- CLASSIC: m-tab 8B EXACTLY pos[6,7,8,9,76,77,78,79] q-indep 256/256, 16/16
  distinct, ALL NEW (m-tails 0/16 vs P182M; IN PLACE).
- q-tab 8B EXACTLY pos[48,49,50,51,72,73,74,75] m-indep 256/256, 16/16
  distinct (tails RELOCATED 76..79->72..75). 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 full-8B (122nd)
- R180-q[i] == P182-M[i] full 8B all 16, zero breaks: heads b48-51 IN PLACE
  16/16 positional, tails relocated 76..79->72..75 16/16 positional.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x4b+2off)&FF 256/256; b5=0x72+(off>=91)+(off>=219) 256/256 (dbl-carry).
- Edges 80255->80256 ff/72->01/73, 80383->80384 ff/73->01/74 as writer.
- varpos EXACTLY tabs+{4,5} (18), 66 consts, 0 stragglers. NO D-class dips.
- Next tier @80421: PB0 ce020000 (repeat of P182 PB0), PB1 ada10500,
  PBA 80423..80424 sig a81a5a00 — all 3 as writer.

## geometry agrees on all 3 legs
