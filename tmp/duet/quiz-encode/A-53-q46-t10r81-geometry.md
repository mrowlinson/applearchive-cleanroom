# A-53 (Q-46): T10R81 R81A alt-row quad + R81B geometry — DERIVED

Bed: census cells N=45273..45620 on disk (own bed, payload
.rav[12:-4]). 45301..45620 all 80B. First-hand this shift;
PRE-1247b/1248b values re-derived byte-exact (all rows TRUE).

## 1. R81B 6B q-tab: VERBATIM R81A m-tab 16/16, zero breaks
- q-tab pos[24,25,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R81B-q[i] == R81A-m[i] byte-for-byte all 16 positional
  (M00 133cabe70d4f .. M15 cc7ccea55065). NO break row.
  (23rd verbatim instance this era.)

## 2. ALT-ROW sigs EXACT all rows; b0,b1 tabbed
- q0: b4394400 x16; q1: 073a4400 x16; q2: b4394400 x16;
  q3: 073a4400 x16 (first-hand per-row counts).
- b0,b1 TABBED: inside 11B sig-led q-tab
  pos[0,1,11,18,19,20,21,76..79], m-indep 4/4 with them.
  Q0/Q2 share 4B b4391b; Q1/Q3 share 4B 073aa9.
- q-tab rows all-NEW (rows re-derived == PRE-1247b).
- Full-80B sweep: A m-only EXACTLY {24,25,72-75}, q-only
  EXACTLY {0,1,11,18,19,20,21,76-79}, both={4,5}.
  Zero stragglers.

## 3. R81A 11B q-tab: NEW rows, B-Q#29 overlap only
- vs P82B m-tab (PBB 11B pos[0,1,11,18,19,20,21,76..79],
  7-sig, 10/10 distinct): 0/4 full-row reuse EITHER direction.
- B-Q#29 (B embeds Q-sub, shared 11B = full qtab, 10 fits,
  first-hand matrix): PBB9-Q1 =5 (a99b7acc21 @pos[11,18,
  19,20,21]); PBB1/4/5-Q0/Q2 =3 (73ac28, 6 fits);
  PBB3-Q1/Q3 + PBB9-Q3 =3 (7acc21, 3 fits).
  All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1247b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0xeb+2off)&FF 64/64 (wraps inside q0 row),
  b5=0x61+(off>=11) 64/64 (single step, q0m11
  carry-forward). Edge 45311 255/97 -> 45312 1/98.
- B: b4=(0x6b+2off)&FF 256/256 (wraps inside q4/q12 rows),
  b5=0x62+(off>=75)+(off>=203) 256/256. Edges 45439
  255/98->1/99; 45567 255/99->1/100 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {22,30,31,72-75},
  q-only EXACTLY {24,25,68-71}, both={4,5}. m-tab 7B
  all-NEW (rows re-derived == PRE-1248b).
- dip scan 45301..45620: A sigs alt-row exact 64/64;
  B sig single 0c7c2c04 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + alt-rows + edges as writer observed.
