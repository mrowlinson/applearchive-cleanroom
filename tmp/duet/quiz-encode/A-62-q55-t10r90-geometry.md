# A-62 (Q-55): T10R90 single-zone geometry — DERIVED

Bed: census cells N=48433..48752 on disk (own bed, payload
.rav[12:-4]). All 80B. First-hand this shift; PRE-1265b/
1266b M rows re-derived byte-exact (TRUE).

## 1. single 16x16 zone: CONFIRM
- 256/256 96B/80B, single sig d37cb2ba (first-hand set
  size 1). NO head singletons.
- m-tab EXACTLY pos[38,39,46,47,72,73,74,75], q-indep
  256/256, 16/16 distinct, ALL NEW (rows == PRE-1266b).
- q-tab EXACTLY pos[40,41,68,69,70,71], m-indep 256/256,
  16/16 distinct.

## 2. verbatim reuse 16/16 positional: CONFIRM (31st instance)
- R90-q[i] == P91M[i] full 6B byte-for-byte all 16
  (P91M re-derived first-hand from 48433..48496, == PRE;
  tails relocated 72..75 -> 68..71). Zero breaks.

## 3. m-prefix sub-structure: CONFIRM
- b38,39 = ef1e m0-12 / 571f m13-15 EXACT 16/16.

## 4. b5 rule + dips: NONE
- b4=(0xe3+2off)&FF 256/256 (wraps inside q0/q8 rows);
  b5=0x7a+(off>=15)+(off>=143) 256/256 (dbl-carry).
  Edges as writer observed: 48511 255/122 -> 48512 1/123;
  48639 255/123 -> 48640 1/124 (b5 set {122,123,124}).
- varpos EXACTLY tabs+{4,5}, 0 stragglers; 0
  tab-violation cells; sig single 256/256. NO D-class dips.

## geometry agrees on all 4 legs
