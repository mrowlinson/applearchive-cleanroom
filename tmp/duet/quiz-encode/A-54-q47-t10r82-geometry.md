# A-54 (Q-47): T10R82 R82A quad + R82B sig-reuse geometry — DERIVED

Bed: census cells N=45621..45968 on disk (own bed, payload
.rav[12:-4]). 45649..45968 all 80B. First-hand this shift;
PRE-1249b/1250b values re-derived byte-exact (all rows TRUE).

## 1. R82B 6B q-tab: VERBATIM R82A m-tab 16/16, zero breaks
- q-tab pos[40,41,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R82B-q[i] == R82A-m[i] byte-for-byte all 16 positional
  (M00 22bcae9dcd6d .. M15 27fc755beff1). NO break row.
  (24th verbatim instance this era.)

## 2. sig reuse EXACT, zero per-zone difference
- R82B (45713..45968): single sig 0c7c2c04 256/256.
- R81B (45365..45620): single sig 0c7c2c04 256/256.
- b0-3 const in both zones, byte-identical. No per-zone
  sig-byte difference anywhere (1st sig reuse this era).

## 3. R82A 11B q-tab: NEW rows, B-Q#30 overlap only
- q-tab pos[25,26,27,33,34,35,37,76..79] (Q0/Q2 share 4B
  803a42; Q1/Q3 share 8B d09543e03c4be4), q-indep 4/4.
- vs P83B m-tab (PBB 15B pos[1,2,22,23,33..39,76..79],
  4-sig b1, 10/10 distinct): 0/4 full-row reuse EITHER
  direction.
- B-Q#30 (B embeds Q-sub, shared 8B pos[33,34,35,37,
  76..79]; b1,b2+22,23,36,38,39 correctly excluded,
  36/38/39 const in quad; 7 fits SUBSTR=3 @pos[33,34,35],
  first-hand matrix): PBB1/4/5-Q0 002fab (3 fits);
  PBB3/9-Q1/Q3 e03c4b (4 fits). All other pairs <=2.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1249b); P-relationship is B-Q
  substring overlap, NOT row reuse.

## 4. b5 rules + dips: NONE
- A: b4=(0xa3+2off)&FF 64/64 (wraps inside q2 row),
  b5=0x64+(off>=47) 64/64 (single step, q2m15
  carry-forward). Edge as writer observed: 45695
  255/100 -> 45696 1/101.
- B: b4=(0x23+2off)&FF 256/256 (wraps inside q6/q14 rows),
  b5=0x65+(off>=111)+(off>=239) 256/256. Edges 45823
  255/101->1/102; 45951 255/102->1/103 (dbl-carry).
- Full-80B sweeps: A m-only EXACTLY {40,41,72-75}, q-only
  EXACTLY {25,26,27,33,34,35,37,76-79}, both={4,5};
  B m-only EXACTLY {38,39,46,47,72-75}, q-only EXACTLY
  {40,41,68-71}, both={4,5}. Zero stragglers. m-tabs
  6B/8B all-NEW (rows re-derived == PREs).
- dip scan 45649..45968: A sig single aff44b00 64/64;
  B sig single 0c7c2c04 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + sig reuse + edges as writer observed.
