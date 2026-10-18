# A-47 (Q-40): T10R75 R75A quad + R75B geometry — DERIVED

Bed: census cells N=43185..43534 on disk (own bed, payload
.rav[12:-4]). 43185..43532 all 80B. First-hand this shift;
PRE-1235b/1236b values re-derived byte-exact (M/Q rows TRUE).

## 1. R75A quad 9B q-tab: NEW rows, B-Q#25 overlap only
- q-tab pos[6,7,8,9,10,76,77,78,79], q-indep 4/4:
  Q0 265919a7f71df7df19 / Q1 d459798e94fdf48c9b /
  Q2 265919a7f7163c081c / Q3 d258b99b3230f1d1ae.
- vs P76B m-tab (PBB 10B pos[6..11,76..79], 10/10 distinct):
  0/4 full-row reuse EITHER direction. Longest shared
  substring = 5B (PBB6/PBB9-Q1 d459798e94), below 9B width.
- B-Q#25 (B embeds Q-sub, 6 fits, first-hand matrix):
  PBB6/9-Q1 SUBSTR=5; PBB2/3-Q3 SUBSTR=4 (58b99b32);
  PBB4-Q0/Q2 SUBSTR=4 (5919a7f7). All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1235b); P-relationship is B-Q
  substring overlap, NOT R<-P-mtab row reuse.

## 2. R75B 7B q-tab: VERBATIM R75A m-tab, 16/16, zero breaks
- q-tab pos[13,14,15,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R75B-q[i] == R75A-m[i] byte-for-byte all 16 positional
  (M00 cf3cb180bcadd4 .. M15 8f3cb2fcfa0d67). NO break row.
- R75A m-tab itself: pos[13,14,15,72,73,74,75], q-indep 4/4,
  16/16 distinct, all-NEW (PRE-1235b, rows re-derived TRUE).

## 3. sig-led m-tab + dips: NONE
- b0 EXACT: 0x65 m0..7 / 0xbd m8..15 (all 256 cells).
- b11 TABBED (in 8B m-tab pos[0,11,18,19,72..75], q-indep
  16/16 with it): 14x 0xc2 + 2x 0x82 at m8/m9 only —
  near-const tab byte, m8/m9-pair marker behavior.
- m-tab rows all-NEW 16/16 distinct (PRE-1236b rows re-derived TRUE).
- b4/b5 rules EXACT: quad b4=(0x9b+2off)&FF 64/64,
  b5=0x51+(q3&m>=3) 64/64; B b4=(0x1b+2off)&FF 256/256,
  b5=0x52+(off>=115)+(off>=243) 256/256. Both wrap edges
  as writer observed (43391 255/82->1/83; 43519 255/83->1/84).
- dip scan 43213..43532: A sig single 4d680e00 64/64, b5 in
  {81,82}; B sig b1-3 const 256/256, b5 in {82,83,84};
  0 tab-violation cells. NO D-class dips.

## geometry agrees
- Quad m7/q9 + B m8/q7 positions exactly as writer observed.
- 43533/43534 singletons cd01/5acc01 confirmed (next zone).
