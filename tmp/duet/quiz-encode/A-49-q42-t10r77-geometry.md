# A-49 (Q-42): T10R77 R77A quad + R77B geometry — DERIVED

Bed: census cells N=43881..44228 on disk (own bed, payload
.rav[12:-4]). 43909..44228 all 80B. First-hand this shift;
PRE-1239b/1240b values re-derived byte-exact (all rows TRUE).

## 1. R77B 8B q-tab: VERBATIM R77A m-tab 16/16, zero breaks
- q-tab pos[37,38,46,47,72,73,74,75] (SAME positions as
  quad m-tab), m-indep 16/16, 16/16 distinct.
- R77B-q[i] == R77A-m[i] byte-for-byte all 16 positional
  (M00 7e262119e2793717 .. M15 fe2721f160779ac5).
  NO break row. (20th verbatim instance this era.)

## 2. swapped sides EXACT, zero stragglers
- Full-80B varying-only sweep first-hand: B m-only EXACTLY
  {6,7,68,69,70,71}, q-only EXACTLY {37,38,46,47,72,73,74,75},
  both={4,5} only.
- m-tab 6B q-indep 16/16, 16/16 distinct, all-NEW
  (rows re-derived == PRE-1240b).
- A likewise exact: m-only {37,38,46,47,72-75}, q-only
  {40-45,76-79}, both={4} (b5 const).

## 3. R77A 10B q-tab: all-NEW, not even B-Q overlap
- q-tab pos[40..45,76..79] (Q0 fffca51becf844333714,
  Q1 427ca0f9ccf245f1458b, Q2 797c55d1ecfe1bfb3c2a,
  Q3 617c9767ecec16738f1d), q-indep 4/4.
- vs P78B m-tab (PBB 18B pos[1,2,36..47,76..79],
  interleaved-sig, 10/10 distinct): 0/4 full-row reuse
  EITHER direction; B-Q max contiguous SUBSTR = 2
  (first-hand 10x4 matrix, all cells <=2) — NO fit.
- verdict: q-tab all-NEW as rows (also 0/4 + 0 sub>=5B vs
  pre-zone corpus per PRE-1239b); no P-relationship at all.

## 4. b5 rules + dips: NONE
- A: b4=(0x0b+2off)&FF 64/64, b5 const 0x57 64/64.
- B: b4=(0x8b+2off)&FF 256/256,
  b5=0x57+(off>=59)+(off>=187) 256/256. Wrap edges
  44031 255/87->1/88; 44159 255/88->1/89 (dbl-carry).
- dip scan 43909..44228: A sig single f3120b00 64/64;
  B sig single 3c2fb100 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees
- All tab positions + swap sides exactly as writer observed.
