# A-87 (Q-81): T10R103 R-zone geometry — DERIVED

Bed: census cells N=53369..53624 on disk (own bed, payload
.rav[12:-4]). First-hand this shift.

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig 2b000000 (NEW). 12th 100B
  zone. NO head singletons.
- m-tab EXACTLY pos[13,14,76,77,78,79], q-indep 256/256,
  16/16 distinct. q-tab EXACTLY pos[6,7,72,73,74,75],
  m-indep 256/256, 16/16 distinct.
- b8 q-step: 0x98 q<=10 else 0xb8, 256/256.

## 2. verbatim reuse 16/16 positional: CONFIRM (46th)
- R103-q[i] == P105-M[i] bytes[0:2]+[3:7] all 16 (P105M
  tails b76..79 -> R103 b72..75; P105 quad row0 re-derived
  53305..53320). Zero breaks.

## 3. b5 rule + dips: NONE
- b4=(0xf3+2off)&FF 256/256; b5=0xa0+(off>=7)+(off>=135)
  256/256 (dbl-carry). Edges 53375->53376, 53503->53504
  as writer observed.
- varpos EXACTLY tabs+{4,5,8}, 69 consts, 0 stragglers.
  NO D-class dips.

## geometry agrees on all 3 legs
