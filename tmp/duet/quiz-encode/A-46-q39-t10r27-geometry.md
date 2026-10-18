# A-46 (Q-39): T10R27 R-zone 26573..26828 geometry — DERIVED

Bed: 256 fresh-oracle cells N=26573..26828 (own bed, payload
.rav[12:-4]). 256/256 76B. (Post-hoc confirm: writer
committed e5fb39a before this answer; derivation oracle-first.)

## 1. geometry: YES, exactly as observed — 16x16 m6/q6
- m-varying-only: b18,19,68,69,70,71 (6B m-tab; 16/16
  rows distinct, MINDEP true). head M0 9fb4dfb9f664.
- q-varying-only: b5,13,14,64,65,66,67 (q-tab 6B payload @
  b13,14,64-67 + b5 q-stepped). head Q0 q-pay 3abce90e22c9.
- b4 varies with both (mixed function, not tabbed).

## 2. q-tab vs PSM: FULL reuse, 16/16 positional
- observed Q rows == _T10PSM rows positionally 16/16
  (q0 3abce90e22c9, q7 bbbcb15dc02e, q15 96fc0c9cefac).
  R<-P-mtab full-reuse pattern continues (R21/R22/R24/R25/R26).
- m-tab all-NEW: 0/16 rows shared with R26M set.

## 3. b5: 79/80/81 steps + 2 intra-row flips; NO dips
- b5 = 79 (q0-2) / 80 (q3-10) / 81 (q11-15); intra-row
  flip m2->m3 at exactly N=26624 (q3) and N=26752 (q11).
  same shape as R23 (locus m=3).
- dip scan: 0 odd cells (all 76B, b5 in {79,80,81}) —
  no D markers.

## verdict: 16x16 m6B@18,19,68-71 + q6B@13,14,64-67 + b5;
q = FULL PSM reuse 16/16; b5 flips 26624 + 26752
