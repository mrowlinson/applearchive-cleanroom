# A-237 (Q-231): T10R177 R-zone geometry — DERIVED

Bed: census N=79121..79376 own bed (.rav[12:-4]). First-hand; P179-M from own P179 census
row0 79057..79072 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig d73d5301 NEW. NO head singletons.
- m-tab 8B EXACTLY pos[48,49,50,51,72,73,74,75] q-indep 256/256, 16/16 distinct,
  ALL NEW (m-tails 0/16 vs P179M; RELOCATED 76..79->72..75, tails-swap cont).
- q-tab 9B EXACTLY pos[23,34,35,42,43,76,77,78,79] m-indep 256/256, 16/16 distinct
  (tails IN PLACE). 0 violations.

## 2. verbatim reuse 8/9 + novel b42: CONFIRM
- q[23,34,35,43,76-79] == P179-M full 8B 16/16 POSITIONAL (in place, zero breaks).
- q-b42 novel: 0 positional matches vs P179 M42, 0 set-overlap vs P179 M42,
  0 set-overlap vs all 64 P179 Q-row b42 bytes.

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0x23+2off)&FF 256/256; b5=0x6a+(off>=111)+(off>=239) 256/256 (dbl-carry).
- Edges per-N exact: 79231->79232 ff/6a->01/6b; 79359->79360 ff/6b->01/6c.
- Varpos EXACTLY tabs+{4,5} (19), 65 consts, 0 stragglers. NO D-class dips.
- Next tier @79377: PB0 54010000 (repeat of P178/P179 PB0), PB1 2f630200, PBA fb322600.

## geometry agrees on all 3 legs
