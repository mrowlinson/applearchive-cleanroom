# A-60 (Q-53): T10R88 R88A pair-row quad + R88B variegated geometry — DERIVED

Bed: census cells N=47709..48056 on disk (own bed, payload
.rav[12:-4]). 47737..48056 all 80B. First-hand this shift;
PRE-1261b/1262b M rows re-derived byte-exact (TRUE).

## 1. R88B 8B q-tab: VERBATIM R88A m-tab 16/16, zero breaks
- q-tab pos[6,7,8,9,68,69,70,71], m-indep 16/16, 16/16 distinct.
- R88B-q[i] == R88A-m[i] byte-for-byte all 16 positional
  (tails relocated 72..75 -> 68..71). NO break row.
  (29th verbatim instance this era.)

## 2. sig-led m-tab: byte3 const 0x4a, 12 sigs, cycle exact
- byte3 = 0x4a all 256/256 (first-hand value set {74}).
- 12/12 distinct sigs; sig = f(m) ONLY — perfect 16-cycle
  (per-m sig const across all 16 q, asserted 16/16).
- cycle m00..m15: e0c55b4a 70c75b4a 70c75b4a 70c85b4a
  70c85b4a 90ca5b4a e0cb5b4a 40cc5b4a 50cc5b4a 50cc5b4a
  10cd5b4a d0ce5b4a d0ce5b4a 30cf5b4a 80c05f4a 40c25f4a
  (== PRE-1262b). m-tab 7B all-NEW (rows == PRE).

## 3. pair-rows: EVEN-ROW 6B SHARED with PBB (8 fits); tails NEW
- Pair-rows f(r&1) EXACT 64/64: row-const 16/16 all rows +
  row0==row2 (350b4bd177fa) / row1==row3 (315f57dac976)
  in (b27,37,38,39,46,47) order (== PRE-1261b print).
- B-Q HIT (not MISS): even pair-row 6B 350b4bd177fa appears
  VERBATIM in PBB2/4/5/6 → 8 fits SUBSTR=6 (4 PBB x AQ0/AQ2)
  on shared 10B pos[27,37,38,39,46,47,76..79] (first-hand
  matrix; tied longest B-Q ever with #26 max-6). Odd
  pair-row unique (max SUBSTR=1 vs all PBB).
- 0/4 full-row reuse either way (10B rows differ in tails).
- tails per-row: 5e5815ec / c91d52cf / 835915ec / ee1e52cf
  — 4/4 distinct; pairs share LAST 2B only (15ec, 52cf).
  tails-vs-M max contig = 1B → all-NEW. (Consistent with
  PRE-1261b B-Q#34 MISS on its tails-vs-Q2 scheme; the
  pair-row-6B fits are on the full shared-10B orientation.)
- verdict: q-structure PARTIALLY shared (even pair-row 6B
  in PBB), tails + odd pair-row all-NEW.

## 4. b5 rules + dips: NONE
- A: b4=(0xf3+2off)&FF 64/64 (wraps row0m6->m7),
  b5=0x74+(off>=7) 64/64 (early bump, holds rest).
  Edge as writer observed: 47743 255/116 -> 47744 1/117.
- B: b4=(0x73+2off)&FF 256/256 (wraps inside q4/q12 rows),
  b5=0x75+(off>=71)+(off>=199) 256/256. Edges 47871
  255/117->1/118; 47999 255/118->1/119 (dbl-carry).
- Full-80B sweeps: A m-only EXACTLY {6,7,8,9,72-75},
  q-only {27,37,38,39,46,47,76-79}, both={4,5};
  B m-only EXACTLY {0,1,2,72-75}, q-only EXACTLY
  {6,7,8,9,68-71}, both={4,5}. Zero stragglers.
- dip scan 47737..48056: A sig single dea76904 64/64;
  B sigs 12-cycle exact 256/256; 0 tab-violation cells.
  NO D-class dips.

## geometry agrees (except Q3 caveat)
- Tab positions + sig cycle + edges as writer observed.
- Q3 caveat: even pair-row is PBB-shared, not all-NEW.
