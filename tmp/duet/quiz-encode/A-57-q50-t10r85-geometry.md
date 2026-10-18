# A-57 (Q-50): T10R85 R85A quad + R85B swapped geometry — DERIVED

Bed: census cells N=46665..47012 on disk (own bed, payload
.rav[12:-4]). 46693..47012 all 80B. First-hand this shift;
PRE-1255b/1256b values re-derived byte-exact (all rows TRUE).

## 1. R85B 6B q-tab: VERBATIM R85A m-tab 16/16, zero breaks
- q-tab pos[46,47,72,73,74,75] (SAME positions as quad
  m-tab), m-indep 16/16, 16/16 distinct.
- R85B-q[i] == R85A-m[i] byte-for-byte all 16 positional
  (M00 3ef97e3c4220 .. M15 8aff0ef9c44e). NO break row.
  (26th verbatim instance this era.)

## 2. swapped sides EXACT, zero stragglers
- Full-80B varying-only sweep first-hand: B m-only EXACTLY
  {6,7,8,68,69,70,71}, q-only EXACTLY {46,47,72,73,74,75},
  both={4,5} only.
- m-tab 7B q-indep 16/16, 16/16 distinct, all-NEW
  (rows re-derived == PRE-1256b).
- A likewise exact: m-only {46,47,72-75}, q-only
  {15,27,37,39,44,76-79}, both={4,5}.

## 3. R85A 9B q-tab: all-NEW, not even B-Q overlap
- q-tab pos[15,27,37,39,44,76..79] (Q0/Q2 share 5B
  76454fcad1; Q1/Q3 share 4B 16513b852b), q-indep 4/4.
- vs P86B m-tab (PBB 11B pos[40..46,76..79], uniform-sig,
  10/10 distinct): 0/4 full-row reuse EITHER direction;
  B-Q max contiguous SUBSTR = 1 on shared 5B
  pos[44,76..79] (first-hand 10x4 matrix, all cells <=1;
  40..43,45,46 correctly excluded — quad mpos/const) — NO fit.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1255b); no P-relationship at all.

## 4. b5 rules + dips: NONE
- A: b4=(0xcb+2off)&FF 64/64 (wraps inside q1 row),
  b5=0x6c+(off>=27) 64/64 (single step, q1m11
  carry-forward). Edge as writer observed: 46719
  255/108 -> 46720 1/109.
- B: b4=(0x4b+2off)&FF 256/256 (wraps inside q5/q13 rows),
  b5=0x6d+(off>=91)+(off>=219) 256/256. Edges 46847
  255/109->1/110; 46975 255/110->1/111 (dbl-carry).
- dip scan 46693..47012: A sig single 4dfc7e01 64/64;
  B sig single d0c4ef17 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + swap sides + edges as writer observed.
