# A-61 (Q-54): T10R89 single-zone geometry — DERIVED

Bed: census cells N=48085..48404 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift; PRE-1263b/
1264b M/Q rows re-derived byte-exact (TRUE).

## 1. single 16x16 zone: CONFIRM
- 256/256 96B/80B, single sig d37cb254 (first-hand set
  size 1). NO head singletons.
- m-tab EXACTLY pos[29,30,31,72,73,74,75], q-indep
  256/256, 16/16 distinct, ALL NEW (rows == PRE-1264b).
- q-tab EXACTLY pos[14,22,23,68,69,70,71], m-indep
  256/256, 16/16 distinct (rows == PRE-1264b).

## 2. tail-4 reuse 16/16 positional: CONFIRM (30th instance)
- R89-q[i][68..71] == P90M[i][72..75] byte-for-byte all 16
  (P90M re-derived first-hand from 48085..48148, == PRE).
- q-prefixes (b14/22/23) NEW vs corpus per PRE; note
  within-zone prefix collisions: 72b179 shared q1/q2,
  7ab179 shared q13/q14 (14 distinct prefixes; full 7B
  q-rows still 16/16 via tails).

## 3. sub-structure: CONFIRM verbatim
- b14 = 0x72 q0-8 / 0x7a q9-15 (72x9,7ax7) EXACT.
- b23 = 79x3,f8,f9x5,78x4,79x2,f8 EXACT (hex
  797979f8f9f9f9f9f9787878787979f8).

## 4. b5 rule + dips: NONE
- b4=(0x2b+2off)&FF 256/256 (wraps inside q6/q14 rows);
  b5=0x78+(off>=107)+(off>=235) 256/256 (dbl-carry).
  Edges as writer observed: 48255 255/120 -> 48256 1/121;
  48383 255/121 -> 48384 1/122 (b5 set {120,121,122}).
- varpos EXACTLY tabs+{4,5}, 0 stragglers; 0
  tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 4 legs
