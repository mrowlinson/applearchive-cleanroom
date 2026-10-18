# GATE-4c5b869 sweep: PASS-individual (rgram 3256/3256; T10R28 ->27176)

- tip: lanes/encode-writer2 @4c5b869 (parent 305959d gated).
  rgram +42/-0 pure addition, for-list +8 cells, pins +16 rows.
- code read (FULL): T10R28 16x16 76B (m-tab 16x7B b33-35,68-71 NEW +
  q-tab = _T10PTM[q] REUSE 16x7B b28-30,64-67 + b5 0xd2+
  (off>=87)+(off>=215) dbl-carry). counts AST-verified (16/60;
  hex width 14; PTM width 14 confirmed; const idx sorted, no dups,
  max 75). const-vs-tab disjoint + FULL cover (60+14+2=76).
  dispatch after PTQ, chain continuous, no neighbor edits. for-list
  straddles BOTH carry edges (86/87, 214/215) + off0/255.
- battery: GATE-PASS shipped legs (outdir gate-w2-4c5b869-s12):
  all green incl PINS set-eq 284/47/181/3256; RGRAM n=3256
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3257 pins" but csv + battery = 3256 (3240+16). off-by-one
  (18th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 26950, 27050, 27100, 27150, 27170.
- boundaries: 26920 pinned PTQ still GREEN; 27177 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 210/211 PASS-individual (w2) + cport 18 PASS-functional.
