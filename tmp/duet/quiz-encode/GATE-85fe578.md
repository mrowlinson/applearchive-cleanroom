# GATE-85fe578 sweep: PASS-individual (rgram 3040/3040; T10R22 ->25088)

- tip: lanes/encode-writer2 @85fe578 (parent 64d23ac gated).
  rgram +43/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R22 16x16 76B (m-tab 16x7B b24-26,52-55 NEW +
  q-tab = _T10PNM[q] REUSE 16x6B b18,19,72-75 + b5 0xc2+
  (off>=127)+(off>=255) dbl-carry). counts AST-verified (16/61;
  hex width 14; PNM width 12 confirmed; const idx sorted, no dups,
  max 71). const-vs-tab disjoint + FULL cover (61+13+2=76).
  dispatch after PNQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (126/127/128 triple, 254/255) + off0.
- battery: GATE-PASS shipped legs (outdir gate-w2-85fe578-s12):
  all green incl PINS set-eq 284/47/181/3040; RGRAM n=3040
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3041 pins" but csv + battery = 3040 (3024+16). off-by-one
  (6th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 24850, 24900, 25000, 25050, 25080.
- boundaries: 24832 pinned PNQ still GREEN; 25089 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 198/199 PASS-individual (w2) + cport 0/9-held.
