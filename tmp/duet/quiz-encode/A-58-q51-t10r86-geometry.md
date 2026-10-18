# A-58 (Q-51): T10R86 R86A distinct-row quad + R86B geometry — DERIVED

Bed: census cells N=47013..47360 on disk (own bed, payload
.rav[12:-4]). 47041..47360 all 80B. First-hand this shift;
PRE-1257b/1258b values re-derived byte-exact (all rows TRUE).

## 1. R86B 7B q-tab: TAIL-4B reuse 16/16, zero full rows
- q-tab pos[16,17,18,72,73,74,75] (q@16..18 FIRST USE),
  m-indep 16/16, 16/16 distinct.
- R86B-q[i] = 3B-new-prefix + R86A-m[i] bytes[2:6] verbatim,
  all 16 positional (e.g. BQ00 e25d3b+b6776b9d,
  BQ15 56db40+aeb56e39). NO break, NO full-row reuse.

## 2. b18 row-split EXACT; sole mixed byte; q-tab stays 9B
- rows1-3 = BASE[m] 48/48, row0 = BASE[m]+1 16/16, with
  BASE = 29 b9 79 99 c9 d9 99 09 09 b9 f9 69 79 79 c9 69
  (writer's table confirmed). 0 violations over 64/64.
- Full-80B sweep: quad both-bytes = {4, 5, 18} (b4
  counter, b5 rule, b18 split). NO other mixed byte.
- b18 is row-split MIXED, not q-tabbed: keep q-tab 9B
  pos[0,1,2,16,17,76..79] + separate b18 rule (answers
  writer's "10B with b18?" — NO).
- Row sigs 4-DISTINCT exact: q0 4a7ce402 x16 (b16,17 =
  33,03), q1 9dbc5602 x16 (01,ab), q2 277c4502 x16
  (cf,d6), q3 9ebc5602 x16 (01,ab).

## 3. R86A 9B q-tab: all-NEW, not even B-Q overlap
- q-tab sig-led 9B (Q0 4a7ce43303b2b05760,
  Q1 9dbc5601ab08389c44, Q2 277c45cfd6fcb25f7d,
  Q3 9ebc5601ab2a7b4953), q-indep 4/4.
- vs P87B m-tab (PBB VPOS [4,13-18,76..79], uniform-sig):
  0/4 full-row reuse EITHER direction on shared 6B
  pos[16,17,76..79] (first-hand check).
- B-Q max contiguous SUBSTR = 2 (first-hand 10x4 matrix,
  all cells <=2) — NO fit. (Consistent with PRE-1257b
  B-Q#32 MISS: tails/M cross-checks 0/4 both ways.)
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1257b); no P-relationship at all.

## 4. b5 rules (last-cell bump) + dips: NONE
- A: b4=(0x83+2off)&FF 64/64 (wraps row3m14->m15),
  b5=0x6f+(off>=63) 64/64 — bump on LAST CELL ONLY.
  Edge 47103 255/111 -> 47104 1/112.
- B: b4=(0x03+2off)&FF 256/256 (wraps inside q7/q15 rows),
  b5=0x70+(off>=127)+(off>=255) 256/256. Edges 47231
  255/112->1/113; 47359 255/113->1/114 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {24,25,26,27,68-71}
  (m@24..27 FIRST USE), q-only EXACTLY {16,17,18,72-75},
  both={4,5}. m-tab 8B all-NEW (rows == PRE-1258b).
- dip scan 47041..47360: A sigs 4-distinct exact 64/64;
  B sig single 11fc3728 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + row-split + edges as writer observed.
