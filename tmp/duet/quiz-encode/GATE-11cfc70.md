# GATE-11cfc70 sweep: PASS-individual (rgram 3148/3148; T10R25 ->26132)

- tip: lanes/encode-writer2 @11cfc70 (parent 4b30e1e gated).
  rgram +42/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R25 16x16 76B (m-tab 16x7B b28-30,68-71 NEW +
  q-tab = _T10PQM[q] REUSE 16x7B b21-23,64-67 + b5 0xca+
  (off>=107)+(off>=235) dbl-carry). counts AST-verified (16/60;
  hex width 14; PQM width 14 confirmed; const idx sorted, no dups,
  max 75). const-vs-tab disjoint + FULL cover (60+14+2=76).
  dispatch after PQQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (106/107, 234/235) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-11cfc70-s12):
  all green incl PINS set-eq 284/47/181/3148; RGRAM n=3148
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3149 pins" but csv + battery = 3148 (3132+16). off-by-one
  (12th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 25900, 26000, 26050, 26100, 26120.
- boundaries: 25876 pinned PQQ still GREEN; 26133 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 204/205 PASS-individual (w2) + cport 14 PASS-functional.
