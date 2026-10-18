# GATE-64d23ac sweep: PASS-individual (rgram 3024/3024; T10P23 ->24832)

- tip: lanes/encode-writer2 @64d23ac (parent f67973d gated).
  rgram +167/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PN0/PN1 singletons (72/76B) + PNA 16x5B
  b13,68-71 + PNB 10x11B b8-10,14-17,72-75 (76B pay) + PNQ 4x16 76B
  (PNM 16x6B b18,19,72-75 + PNQ-tab 4x11B b8-10,14-17,68-71 +
  b5 0xc1+(off>=63)). counts AST-verified (71/75/16/70/10/64/16/4/57;
  hex widths 10/22/12/22; const idx sorted, no dups). const-vs-tab
  disjoint + FULL cover every tier (71+1/75+1/70+5+1/64+11+1/
  57+6+11+1+1). dispatch continuous 24740->24832, no neighbor edits.
  for-list straddles all edges incl b5 off62/63.
- battery: GATE-PASS shipped legs (outdir gate-w2-64d23ac-s12):
  all green incl PINS set-eq 284/47/181/3024; RGRAM n=3024
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3025 pins" but csv + battery = 3024 (3004+20). off-by-one
  (5th in series: P21/R20/P22/R21/P23).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 24750 PNA, 24763 PNB, 24780/24800/24820 PNQ.
- boundaries: 24740 pinned R21 still GREEN; 24833 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 197/198 PASS-individual (w2) + cport 0/8-held.
