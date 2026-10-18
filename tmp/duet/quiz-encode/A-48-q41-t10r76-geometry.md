# A-48 (Q-41): T10R76 R76A quad + R76B geometry — DERIVED

Bed: census cells N=43533..43880 on disk (own bed, payload
.rav[12:-4]). 43561..43880 all 80B. First-hand this shift;
PRE-1237b/1238b values re-derived byte-exact (all rows TRUE).

## 1. R76B 9B q-tab: TAIL-4B reuse 16/16, zero full rows
- q-tab pos[24,25,29,30,31,72,73,74,75], m-indep 16/16,
  16/16 distinct.
- R76B-q[i] = 5B-new-prefix + R76A-m[i] bytes[4:8] verbatim,
  all 16 positional (e.g. BQ00 6dd93ff6f7+4e36e6ea,
  BQ10 0ddd9fe777+2a396308). NO break, NO full-row reuse.
- prefixes 13/16 distinct: 6dd9-group q0-9, 0ddd-group
  q10-15 (as writer observed from m0 col).

## 2. swapped sides EXACT, zero stragglers
- Full-80B varying-only sweep first-hand: B m-only EXACTLY
  {26,34,35,68,69,70,71}, q-only EXACTLY
  {24,25,29,30,31,72,73,74,75}, both={4,5} only.
- m-tab 7B q-indep 16/16, 16/16 distinct, all-NEW
  (rows re-derived == PRE-1238b).
- A likewise exact: m-only {21,22,30,31,72-75}, q-only
  {24-29,76-79}, both={4} (b5 const).

## 3. R76A 10B q-tab: NEW rows, B-Q#26 overlap only
- q-tab pos[24..29,76..79] (Q0 903c8173edeef0b8eb1a,
  Q1 bdbc55680de3eab43c85, Q2 6cbc9191edfa9a30514b,
  Q3 c87ca57e4dd747b52c82), q-indep 4/4.
- vs P77B m-tab (PBB 16B pos[1,21..31,76..79], split-sig,
  10/10 distinct): 0/4 full-row reuse EITHER direction.
- B-Q#26 (B embeds Q-sub, 8 fits, first-hand matrix,
  max SUBSTR=6 longest B-Q ever): PBB9-Q1 =6
  (bdbc55680de3); PBB2/6-Q1, PBB1/5/8-Q2, PBB4-Q0,
  PBB3-Q3 =5. All other pairs <=1.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1237b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0x53+2off)&FF 64/64, b5 const 0x54 64/64 (no wrap).
- B: b4=(0xd3+2off)&FF 256/256,
  b5=0x54+(off>=23)+(off>=151) 256/256. Wrap edges as
  writer observed (43647 255/84->1/85; 43775 255/85->1/86).
- dip scan 43561..43880: A sig single f3340700 64/64;
  B sig single f39c6300 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + wrap edges exactly as writer observed.
