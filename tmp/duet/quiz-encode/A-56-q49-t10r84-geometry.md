# A-56 (Q-49): T10R84 R84A xor-quad + R84B geometry — DERIVED

Bed: census cells N=46317..46664 on disk (own bed, payload
.rav[12:-4]). 46345..46664 all 80B. First-hand this shift;
PRE-1253b/1254b values re-derived byte-exact (all rows TRUE).

## 1. R84B 7B q-tab: TAIL-4B reuse 16/16, zero full rows
- q-tab pos[28,29,30,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R84B-q[i] = 3B-new-prefix + R84A-m[i] bytes[3:7] verbatim,
  all 16 positional (e.g. BQ00 31fc4f+e13c6f11 as writer
  observed, BQ07 4dbf53+86fcd012). NO break, NO full-row reuse.

## 2. XOR-BOTH b29 EXACT; sole mixed byte
- pay[29] = M29[m]^(q&1) EXACT 64/64 with M29 = 63 63 63 63
  a3 63 a3 63 63 a3 a3 63 23 a3 a3 e3 (writer's table
  confirmed byte-for-byte).
- Full-80B sweep: quad both-bytes = {4, 29} ONLY (b4
  counter, b29 XOR; b5 const). NO other XOR/mixed byte
  in 46345..46408. (1st XOR-BOTH byte this era.)
- m-only EXACTLY {24,30,31,72-75}, q-only EXACTLY
  {1,2,21,22,23,28,76-79}. Zero stragglers.

## 3. R84A 10B q-tab: NEW rows, not even B-Q overlap
- q-tab pos[1,2,21,22,23,28,76..79] (Q0/Q2 share 7B
  9ba2f3f19ede; Q1/Q3 share 7B 3fa407f0e094), q-indep 4/4.
- vs P85B m-tab (PBB 11B pos[24..30,76..79], uniform-sig,
  10/10 distinct): 0/4 full-row reuse EITHER direction;
  B-Q max contiguous SUBSTR = 1 on shared 5B
  pos[28,76..79] (first-hand 10x4 matrix, all cells <=1;
  24..27,29,30 correctly excluded — quad mpos/BOTH) — NO fit.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1253b); no P-relationship at all.

## 4. b5 rules + dips: NONE
- A: b4=(0x13+2off)&FF 64/64 (no wrap), b5 const 0x6a 64/64.
- B: b4=(0x93+2off)&FF 256/256 (wraps inside q3/q11 rows),
  b5=0x6a+(off>=55)+(off>=183) 256/256. Edges 46463
  255/106->1/107; 46591 255/107->1/108 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {34,35,72-75}, q-only
  EXACTLY {28,29,30,68-71}, both={4,5}. m-tab 6B all-NEW
  (rows re-derived == PRE-1254b).
- dip scan 46345..46664: A sigs alt-row exact (q0,q2
  599ba200 / q1,q3 593fa400) 64/64; B sig single
  4dfc7e0a 256/256; 0 tab-violation cells (incl XOR-b29
  rule in A fit). NO D-class dips.

## geometry agrees
- All tab positions + XOR rule + edges as writer observed.
