# A-55 (Q-48): T10R83 R83A gapped quad + R83B geometry — DERIVED

Bed: census cells N=45969..46316 on disk (own bed, payload
.rav[12:-4]). 45997..46316 all 80B. First-hand this shift;
PRE-1251b/1252b values re-derived byte-exact (all rows TRUE).

## 1. R83B 6B q-tab: VERBATIM R83A m-tab 16/16, zero breaks
- q-tab pos[13,14,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R83B-q[i] == R83A-m[i] byte-for-byte all 16 positional
  (M00 e07c6e453ff6 .. M15 7ebc5c145a98). NO break row.
  (25th verbatim instance this era.)

## 2. b8 gap EXACT (0x19), sole gap in q-span
- b8 = 0x19 all 64/64 (first-hand count). Lone single-gap
  inside the 6..11 run (6,7 vary; 8 const; 9,10,11 vary).
- No other gap: m-span 13,14,72-75 contiguous; remaining
  const bytes in 0..20 are sig (b0-3), b5 (const 0x67),
  and non-tab 12/15-20.
- Full-80B sweep: A m-only EXACTLY {13,14,72-75}, q-only
  EXACTLY {6,7,9,10,11,76-79}, both={4} (b5 const).
  Zero stragglers.

## 3. R83A 9B q-tab: NEW rows, B-Q#31 overlap only
- q-tab pos[6,7,9,10,11,76..79] (Q0/Q2 share 5B
  2d5d3cc9e9; Q1/Q3 share 5B 4c5f4170e8), q-indep 4/4.
- vs P84B m-tab (PBB 10B pos[6..11,76..79], uniform-sig,
  10/10 distinct): 0/4 full-row reuse EITHER direction.
- B-Q#31 (B embeds Q-sub, shared 9B = full qtab; pos8
  correctly excluded — const in quad; 10 fits,
  first-hand matrix): PBB9-Q1/Q3 =4 (4c5f4170 @pos[6,7,
  9,10], 2 fits); PBB1/4/5-Q0/Q2 =3 (5d3cc9, 6 fits);
  PBB3-Q1/Q3 =3 (5f4170, 2 fits). All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1251b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0x5b+2off)&FF 64/64 (no wrap), b5 const 0x67 64/64.
- B: b4=(0xdb+2off)&FF 256/256 (wraps inside q1/q9 rows),
  b5=0x67+(off>=19)+(off>=147) 256/256. Edges 46079
  255/103->1/104; 46207 255/104->1/105 (dbl-carry).
- B full-80B sweep: m-only EXACTLY {18,19,72-75}, q-only
  EXACTLY {13,14,68-71}, both={4,5}. m-tab 6B all-NEW
  (rows re-derived == PRE-1252b).
- dip scan 45997..46316: A sig single e5bf5200 64/64;
  B sig single bdf80b05 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + gap + edges as writer observed.
