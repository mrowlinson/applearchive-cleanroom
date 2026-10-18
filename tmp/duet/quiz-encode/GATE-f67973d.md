# GATE-f67973d sweep: PASS-individual (rgram 3004/3004; T10R21 ->24740)

- tip: lanes/encode-writer2 @f67973d (parent f949df5 gated).
  rgram +45/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R21 16x16 76B (m-tab 16x6B b6,7,68-71 NEW +
  q-tab = _T10PMM[q] REUSE 16x6B b49,50,72-75 + b5 R21B5[m]+
  (off>=91)+(off>=219) dbl-carry). counts AST-verified (16/16/62;
  hex width 12; PMM width 12 confirmed; const idx sorted, no dups,
  max 67). const-vs-tab disjoint + FULL cover (62+12+2=76).
  dispatch after PMQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (90/91, 218/219) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-f67973d-s12):
  all green incl PINS set-eq 284/47/181/3004; RGRAM n=3004
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3005 pins" but csv + battery = 3004 (2988+16). off-by-one
  (4th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 24500, 24600, 24650, 24700, 24720.
- boundaries: 24484 pinned PMQ still GREEN; 24741 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 196/197 PASS-individual (w2) + cport 0/7-held.
