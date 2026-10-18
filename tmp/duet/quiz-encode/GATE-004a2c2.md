# GATE-004a2c2 sweep: PASS-individual (rgram 3292/3292; T10R29 ->27524)

- tip: lanes/encode-writer2 @004a2c2 (parent 5874e49 gated).
  rgram +45/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R29 16x16 76B (m-tab 16x6B b6,7,68-71 NEW +
  q-tab = _T10PUM[q] REUSE 16x6B b46,47,64-67 + b5 B5[m]+
  (off>=123)+(off>=251) mtab {0x55,0xd5}). counts AST-verified
  (16/16/62; hex width 12; PUM width 12 confirmed; const idx
  sorted, no dups, max 75). const-vs-tab disjoint + FULL cover
  (62+12+2=76). dispatch after PUQ, chain continuous, no neighbor
  edits. for-list straddles BOTH carry edges (122/123, 250/251)
  + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-004a2c2-s12):
  all green incl PINS set-eq 284/47/181/3292; RGRAM n=3292
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3293 pins" but csv + battery = 3292 (3276+16). off-by-one
  (20th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 27300, 27400, 27450, 27500, 27522.
- boundaries: 27268 pinned PUQ still GREEN; 27525 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 212/213 PASS-individual (w2) + cport 20 PASS-functional.
