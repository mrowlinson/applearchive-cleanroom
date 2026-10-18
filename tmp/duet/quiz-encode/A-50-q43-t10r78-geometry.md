# A-50 (Q-43): T10R78 R78A m-split quad + R78B geometry — DERIVED

Bed: census cells N=44229..44576 on disk (own bed, payload
.rav[12:-4]). 44257..44576 all 80B. First-hand this shift;
PRE-1241b/1242b values re-derived byte-exact (all rows TRUE).

## 1. R78B 7B q-tab: TAIL-4B reuse 16/16, zero full rows
- q-tab pos[13,18,19,76,77,78,79], m-indep 16/16, 16/16 distinct.
- R78B-q[i] = 3B-new-prefix + R78A-m[i] bytes[4:8] verbatim,
  all 16 positional (e.g. BQ00 e720f5+35fc7652 as writer
  observed, BQ13 e8f0a3+f7fa6815). NO break, NO full-row reuse.

## 2. m-split locus m13 EXACT all 4 q-rows; b0 tabbed
- b0 = 0xf3 m0..12 / 0xf4 m13..15 in EACH of q0-q3
  (first-hand per-row split cols [13,14,15] x4).
- b0 TABBED: inside 8B m-tab pos[0,10,11,19,76..79],
  q-indep 4/4 with it, rows 16/16 distinct (all-NEW,
  rows re-derived == PRE-1241b).
- b10/b11 low-entropy tab bytes: b10 = 0x7d (m0-4, m13-15)
  / 0xfd (m5-12); b11 = 0xdf (m0-12) / 0x5a (m13-15,
  marks f4-group exactly). b19 fully tabbed (11 distinct).
- Full-80B sweep: A m-only EXACTLY {0,10,11,19,76-79},
  q-only EXACTLY {13-18,72-75}, both={4,5}. Zero stragglers.

## 3. R78A 10B q-tab: NEW rows, B-Q#27 overlap only
- q-tab pos[13..18,72..75] (Q0 d27c94541418d0c40bb8,
  Q1 f2fc54d4a81108517546, Q2 d27c94541418ec6024b8
  Q0/Q2 share 6B prefix, Q3 227c63b4810eae51fee2).
- vs P79B m-tab (PBB 10B pos[13..18,76..79], uniform-sig,
  10/10 distinct): 0/4 full-row reuse EITHER direction.
- B-Q#27 (B embeds Q-sub, shared 6B pos[13..18], 7 fits,
  first-hand matrix): PBB9-Q1 =6 (f2fc54d4a811);
  PBB3/6-Q1 =5 (fc54d4a811); PBB1/5-Q0/Q2 =5
  (7c94541418). All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1241b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0xc3+2off)&FF 64/64, b5=0x59+(off>=31) 64/64
  (single step, q1m15 carry-forward). Edge as writer
  observed: 44287 255/89 -> 44288 1/90.
- B: b4=(0x43+2off)&FF 256/256,
  b5=0x5a+(off>=95)+(off>=223) 256/256. Edges 44415
  255/90->1/91; 44543 255/91->1/92 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {24,25,26,68-71},
  q-only EXACTLY {13,18,19,76-79}, both={4,5}. m-tab 7B
  all-NEW (rows re-derived == PRE-1242b).
- dip scan 44257..44576: A b5 in {89,90}; B b5 in
  {90,91,92}; sigs per-side constant; 0 tab-violation
  cells. NO D-class dips.

## geometry agrees
- All tab positions + split locus + edges as writer observed.
