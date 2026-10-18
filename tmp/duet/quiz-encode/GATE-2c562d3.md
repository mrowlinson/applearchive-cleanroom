# GATE-2c562d3 sweep: PASS-individual (rgram 2786/2786; T10R15 22397..22652)

- tip: lanes/encode-writer2 @2c562d3 (parent b6fe0f7 gated).
  rgram +42/-0 (T10R15 branch + tables), for-list +8 pure
  addition, pins +16 rows append-only.
- code read (FULL): _T10R15M 16 lits (m-tab 6B
  b36,37,60-63, AST-verified) + _T10R15C consts; b5 rule
  0xae+(off>=3)+(off>=131) dbl-carry; q-tab 6B reuses
  _T10PGM[q]. carry edges in for-list: 22399/22400
  (off2/3 ae->af), 22527/22528 (off130/131 af->b0).
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-2c562d3-s9):
  RGRAM n=2786, PINS-RGRAM set-eq 2786/2786, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 22398 (off1, ae), 22401 (off4, af),
  22526 (off129, af), 22529 (off132, b0), 22450 (off53,
  af mid) — both carry edges covered both ways.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 183/184 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
