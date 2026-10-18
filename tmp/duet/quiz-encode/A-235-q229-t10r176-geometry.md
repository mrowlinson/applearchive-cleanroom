# A-235 (Q-229): T10R176 R-zone geometry — DERIVED

Bed: census N=78773..79028 own bed (.rav[12:-4]). First-hand; P178-M from own P178 census
row0 78709..78724 (this seat).

## 1. single 16x16 zone, TAILS-SWAP: CONFIRM
- 256/256 100B/84B, single sig 0d235701 NEW. NO head singletons.
- m-tab 8B EXACTLY pos[32,33,34,35,72,73,74,75] q-indep 256/256, 16/16 distinct,
  ALL NEW (m-tails 0/16 vs P178M; RELOCATED 76..79->72..75).
- q-tab 7B EXACTLY pos[24,25,26,76,77,78,79] m-indep 256/256, 16/16 distinct
  (tails IN PLACE). 0 violations.

## 2. partial verbatim reuse: CONFIRM 6/7 bytes, zero breaks
- q-tails == P178-M tails 16/16 POSITIONAL (in place b76-79).
- q-b24 == P178M-b26 + q-b25 == P178M-b27 16/16 positional (relocated 26->24, 27->25).
- q-b26 novel (0/16 vs all P178M heads).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x6b+2off)&FF 256/256; b5=0x67+(off>=75)+(off>=203) 256/256 (dbl-carry).
- Edges per-N exact: 78847->78848 ff/67->01/68; 78975->78976 ff/68->01/69.
- Varpos EXACTLY tabs+{4,5} (17), 67 consts, 0 stragglers. NO D-class dips.
- Next tier @79029: PB0 54010000 (repeat of P178 PB0), PB1 f91e0100, PBA d73d1700.

## geometry agrees on all 3 legs
