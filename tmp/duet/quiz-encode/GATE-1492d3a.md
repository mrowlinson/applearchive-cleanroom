# GATE-1492d3a sweep: PASS-individual (rgram 3204/3204; T10P28 ->26572)

- tip: lanes/encode-writer2 @1492d3a (parent f03ca3b gated).
  rgram +165/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PS0/PS1 singletons (BOTH 76B this head) + PSA
  16x6B b5,6,72-75 (b5-tabbed) + PSB 10x10B b5-10,72-75 + PSQ 4x16
  76B (PSM 16x6B b13,14,68-71 + PSQ-tab 4x10B b5-10,72-75; b5 in
  qtab, no separate rule). counts AST-verified (75/75/16/69/10/
  65/16/4/59; hex widths 12/20/12/20; const idx sorted, no dups).
  const-vs-tab disjoint + FULL cover every tier (75+1/75+1/69+6+1/
  65+10+1/59+6+10+1). dispatch continuous 26480->26572, no neighbor
  edits. for-list straddles all edges incl q0/q1 (off31/32).
- battery: GATE-PASS shipped legs (outdir gate-w2-1492d3a-s12):
  all green incl PINS set-eq 284/47/181/3204; RGRAM n=3204
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3205 pins" but csv + battery = 3204 (3184+20). off-by-one
  (15th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 26490 PSA, 26503 PSB, 26520/26550/26565 PSQ.
- boundaries: 26480 pinned R26 still GREEN; 26573 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 207/208 PASS-individual (w2) + cport 16 PASS-functional.
