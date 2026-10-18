# A-51 (Q-44): T10R79 R79A holed quad + R79B geometry — DERIVED

Bed: census cells N=44577..44924 on disk (own bed, payload
.rav[12:-4]). 44605..44924 all 80B. First-hand this shift;
PRE-1243b/1244b values re-derived byte-exact (all rows TRUE).

## 1. R79B 6B q-tab: VERBATIM R79A m-tab 16/16, zero breaks
- q-tab pos[34,35,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R79B-q[i] == R79A-m[i] byte-for-byte all 16 positional
  (M00 b1ddbcf57032 .. M15 11ee597b8542). NO break row.
  (21st verbatim instance this era.)

## 2. b30 hole EXACT + second gap 26,27
- b30 = 0xfe all 64/64 (first-hand count). Lone single-gap
  inside the 28..33 run (28,29 vary; 30 const; 31,32,33 vary).
- 2nd gap in wider span: b26,b27 const 0xa0/0xbf all 64,
  splitting 24,25 from 28,29. So the 24..33 span carries
  THREE const bytes (26,27,30); convention names b30 the
  HOLE (3rd holed q-tab: P63/P71 b14, P80 b30).
- m-tab span 34,35,72-75 contiguous, no holes. Full-80B
  sweep: A m-only EXACTLY {34,35,72-75}, q-only EXACTLY
  {24,25,28,29,31,32,33,76-79}, both={4} (b5 const).
  B m-only EXACTLY {40,72-75}, q-only EXACTLY
  {34,35,68-71}, both={4,5}. Zero stragglers.
- m-tab 6B q-indep 4/4, 16/16 distinct, all-NEW
  (rows re-derived == PRE-1243b). B m-tab 5B all-NEW
  (rows re-derived == PRE-1244b).

## 3. R79A 11B q-tab: all-NEW, not even B-Q overlap
- q-tab pos[24,25,28,29,31,32,33,76-79] (Q0/Q2 share 8B
  a729ec57fb8e54; Q1 e72fec4ac18e37114140e6,
  Q3 67246c67856e29f762f3d0), q-indep 4/4.
- vs P80B m-tab (PBB 12B pos[21,22,29..34,76..79],
  uniform-sig, 10/10 distinct): 0/4 full-row reuse
  EITHER direction; B-Q max contiguous SUBSTR = 2 on
  shared 8B pos[29,31,32,33,76-79] (first-hand 10x4
  matrix, all cells <=2) — NO fit.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1243b); no P-relationship at all.

## 4. b5 rules (early wrap YES) + dips: NONE
- A: b4=(0x7b+2off)&FF 64/64 (no wrap), b5 const 0x5c 64/64.
- B: b4=(0xfb+2off)&FF 256/256 (wraps inside q0/q8 rows),
  b5=0x5c+(off>=3)+(off>=131) 256/256 — early wrap at
  off>=3 CONFIRMED (q0m3). Edges 44671 255/92->1/93;
  44799 255/93->1/94 (dbl-carry).
- dip scan 44605..44924: A sig single d15f1c00 64/64;
  B sig single 559ed501 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + hole + early wrap as writer observed.
