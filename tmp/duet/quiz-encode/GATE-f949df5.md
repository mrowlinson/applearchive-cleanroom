# GATE-f949df5 sweep: PASS-individual (rgram 2988/2988; T10P22 ->24484)

- tip: lanes/encode-writer2 @f949df5 (parent 055bb85 gated).
  rgram +165/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PM0/PM1 singletons (72/76B) + PMA 16x7B
  b41-43,64-67 + PMB 10x9B b40-44,64-67 + PMQ 4x16 76B (PMM 16x6B
  b49,50,72-75 + PMQ-tab 4x9B b44-48,68-71 + b5 0xbe+(off>=27)).
  counts AST-verified (71/75/16/68/10/62/16/4/59; hex widths
  14/18/12/18; const idx sorted, no dups). const-vs-tab disjoint +
  FULL cover every tier (71+1/75+1/68+7+1/62+9+1/59+6+9+1+1).
  dispatch continuous 24392->24484, no neighbor edits. for-list
  straddles all edges incl b5 off26/27.
- battery: GATE-PASS shipped legs (outdir gate-w2-f949df5-s12):
  all green incl PINS set-eq 284/47/181/2988; RGRAM n=2988
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "2989 pins" but csv + battery = 2988 (2968+20). off-by-one
  (3rd in series: P21/R20/P22).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 24400 PMA, 24415 PMB, 24430/24460/24475 PMQ.
- boundaries: 24392 pinned R20 still GREEN; 24485 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 195/196 PASS-individual (w2) + cport 0/5-held.
