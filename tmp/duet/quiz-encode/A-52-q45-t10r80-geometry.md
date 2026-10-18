# A-52 (Q-45): T10R80 R80A alt-row quad + R80B geometry — DERIVED

Bed: census cells N=44925..45272 on disk (own bed, payload
.rav[12:-4]). 44953..45272 all 80B. First-hand this shift;
PRE-1245b/1246b values re-derived byte-exact (all rows TRUE).

## 1. R80B 6B q-tab: VERBATIM R80A m-tab 16/16, zero breaks
- q-tab pos[6,7,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R80B-q[i] == R80A-m[i] byte-for-byte all 16 positional
  (M00 fcd8351713c0 .. M15 56db8fc774c3). NO break row.
  (22nd verbatim instance this era.)

## 2. ALT-ROW sigs EXACT all rows; b1,b2 tabbed
- q0: 107d1700 x16; q1: 10fd1600 x16; q2: 107d1700 x16;
  q3: 10fd1600 x16 (first-hand per-row counts).
- b1,b2 TABBED: inside 11B sig-led q-tab
  pos[1,2,37,38,39,46,47,76..79], m-indep 4/4 with them.
  Q0/Q2 share 5B 7d172e314d; Q1/Q3 share 2B sig fd16.
- q-tab rows all-NEW (rows re-derived == PRE-1245b).
- Full-80B sweep: A m-only EXACTLY {6,7,72-75}, q-only
  EXACTLY {1,2,37,38,39,46,47,76-79}, both={4} (b5 const).
  Zero stragglers.

## 3. R80A 11B q-tab: NEW rows, B-Q#28 overlap only
- vs P81B m-tab (PBB 10B pos[1,37,38,39,46,47,76..79],
  3-sig, 10/10 distinct): 0/4 full-row reuse EITHER direction.
- B-Q#28 (B embeds Q-sub, shared 10B = q-tab minus b2
  which is const in PBB; 8 fits SUBSTR=3 @pos[37,38,39],
  first-hand matrix): PBB1/4/5-Q0/Q2 2e314d (6 fits);
  PBB3/9-Q1 e6bebb (2 fits). All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1245b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0x33+2off)&FF 64/64 (no wrap), b5 const 0x5f 64/64.
- B: b4=(0xb3+2off)&FF 256/256 (wraps inside q2/q10 rows),
  b5=0x5f+(off>=39)+(off>=167) 256/256. Edges 45055
  255/95->1/96; 45183 255/96->1/97 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {13-16,72-75}, q-only
  EXACTLY {6,7,68-71}, both={4,5}. m-tab 8B all-NEW
  (rows re-derived == PRE-1246b).
- dip scan 44953..45272: A sigs alt-row exact 64/64;
  B sig single 02d17701 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + alt-rows + edges as writer observed.
