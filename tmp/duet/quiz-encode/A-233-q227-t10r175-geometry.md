# A-233 (Q-227): T10R175 R-zone geometry — DERIVED

Bed: census N=78425..78680 own bed (.rav[12:-4]). First-hand; P177-M from own P177 census
row0 78361..78376 (this seat).

## 1. single 16x16 zone: CONFIRM
- 256/256 100B/84B, single sig f8733501 NEW. NO head singletons.
- m-tab 8B EXACTLY pos[13,14,15,16,76,77,78,79] q-indep 256/256, 16/16 distinct,
  ALL NEW (m-tails 0/16 vs P177M; IN PLACE).
- q-tab 8B EXACTLY pos[6,7,8,9,72,73,74,75] m-indep 256/256, 16/16 distinct. 0 violations.

## 2. verbatim reuse: CONFIRM 16/16 positional
- R175-q[i] == P177-M[i] full 8B all 16, zero breaks (heads b6-9 IN PLACE, tails
  relocated 76..79 -> 72..75).

## 3. b5 rule + dips: CONFIRM, NONE
- b4=(0xb3+2off)&FF 256/256; b5=0x64+(off>=39)+(off>=167) 256/256 (dbl-carry).
- Edges per-N exact: 78463->78464 ff/64->01/65; 78591->78592 ff/65->01/66.
- Varpos EXACTLY tabs+{4,5} (18), 66 consts, 0 stragglers. NO D-class dips.
- Next tier @78681: PB0 54010000, PB1 78540100, PBA 8e471500 (all 3 as predicted).

## geometry agrees on all 3 legs
