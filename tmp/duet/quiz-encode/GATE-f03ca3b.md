# GATE-f03ca3b sweep: PASS-individual (rgram 3184/3184; T10R26 ->26480)

- tip: lanes/encode-writer2 @f03ca3b (parent 58da85a gated).
  rgram +42/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R26 16x16 76B (m-tab 16x8B b30,41-43,68-71
  NEW + q-tab = _T10PRM[q] REUSE 16x7B b37-39,60-63 + b5 0xcc+
  (off>=15)+(off>=143) dbl-carry). counts AST-verified (16/59;
  hex width 16; PRM width 14 confirmed; const idx sorted, no dups,
  max 75). const-vs-tab disjoint + FULL cover (59+15+2=76).
  dispatch after PRQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (14/15, 142/143/144) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-f03ca3b-s12):
  all green incl PINS set-eq 284/47/181/3184; RGRAM n=3184
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3185 pins" but csv + battery = 3184 (3168+16). off-by-one
  (14th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 26250, 26300, 26400, 26450, 26470.
- boundaries: 26224 pinned PRQ still GREEN; 26481 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 206/207 PASS-individual (w2) + cport 15 PASS-functional.
