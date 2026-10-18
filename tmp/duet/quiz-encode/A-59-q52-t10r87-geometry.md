# A-59 (Q-52): T10R87 R87A pair-row quad + R87B geometry — DERIVED

Bed: census cells N=47361..47708 on disk (own bed, payload
.rav[12:-4]). 47389..47708 all 80B. First-hand this shift;
PRE-1259b/1260b M rows re-derived byte-exact (TRUE).

## 1. R87B 8B q-tab: PREFIX1B + Am 7B verbatim 16/16
- q-tab pos[25,26,34,35,68,69,70,71] (q@25,26,34,35 FIRST
  USE; q at 68..71), m-indep 16/16, 16/16 distinct.
- R87B-q[i][1:8] == R87A-m[i][0:7] byte-for-byte all 16
  (tails relocated 72..75 -> 68..71). NO break.
- b25 PREFIX rule EXACT: 0x48 all q EXCEPT q3..q7 = 0xc8
  (single contiguous block [3,7]; first-hand per-q:
  48,48,48,c8,c8,c8,c8,c8,48x8).

## 2. pair-row bytes EXACT, zero stragglers; tails all-NEW
- b24,29,31,32,33 = f(r&1) EXACT 64/64: row-constant 16/16
  all 4 rows + row0==row2 / row1==row3. Values in
  (b24,b29,b31,b32,b33) order: even rows (c8,46,cf,ce,56),
  odd rows (a8,c8,e7,2e,3e). (Same value multisets as
  PRE-1259b print; tuple order differs — mine is
  positional first-hand.)
- tails per-row NOT paired: e569cbfe / 1d5c8c3b / ef80cbfe
  / f55d8c3b — 4/4 distinct; pairs share LAST 2B only
  (cbfe, 8c3b). tails-vs-M max contig = 1B → all-NEW.
- Full-80B sweep: A m-only EXACTLY {26,34,35,72-75},
  q-only {24,29,31,32,33,76-79}, both={4,25}. m-tab 7B
  all-NEW (rows re-derived == PRE-1259b).

## 3. b25 (r,m)-rule EXACT; sole mixed byte
- b25 = (0x58-(r&1)*3) + (0x80 iff 3<=m<=7) EXACT 64/64
  (rows0,2: 58/d8; rows1,3: 55/d5 — writer's rule
  confirmed cell-for-cell).
- Quad both-bytes = {4, 25} only (b4 counter, b25 rule;
  b5 const). NO other mixed byte in 47389..47452.

## 4. b5 rules + dips: NONE
- A: b4=(0x3b+2off)&FF 64/64 (no wrap, max 0xb9),
  b5 const 0x72 64/64.
- B: b4=(0xbb+2off)&FF 256/256 (wraps inside q2/q10 rows),
  b5=0x72+(off>=35)+(off>=163) 256/256. Edges 47487
  255/114->1/115; 47615 255/115->1/116 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {40,41,42,43,72-75}
  (m@40..43 FIRST USE; m back at 72..75), q-only EXACTLY
  {25,26,34,35,68-71}, both={4,5}. m-tab 8B all-NEW
  (rows re-derived == PRE-1260b).
- dip scan 47389..47708: A sig single a9bc0402 64/64;
  B sig single a9bc0428 (quad-sig family, 4th byte
  02->28) 256/256; 0 tab-violation cells. NO D-class dips.

## geometry agrees
- All tab positions + pair-rows + b25 rule as writer observed.
