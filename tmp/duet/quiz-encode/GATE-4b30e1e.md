# GATE-4b30e1e sweep: PASS-individual (rgram 3132/3132; T10P26 ->25876)

- tip: lanes/encode-writer2 @4b30e1e (parent 1821f18 gated).
  rgram +167/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PQ0/PQ1 singletons (72/76B) + PQA 16x7B
  b10,18,19,68-71 + PQB 10x10B b10,11,17-20,72-75 + PQQ 4x16 76B
  (PQM 16x7B b21-23,68-71 + PQQ-tab 4x10B b10,11,17-20,72-75 +
  b5 0xc9+(off>=43)). counts AST-verified (71/75/16/68/10/65/
  16/4/57; hex widths 14/20/14/20; const idx sorted, no dups).
  const-vs-tab disjoint + FULL cover every tier (71+1/75+1/
  68+7+1/65+10+1/57+7+10+1+1). dispatch continuous 25784->25876,
  no neighbor edits. for-list straddles b5 edge off42/43 + all
  tier edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-4b30e1e-s12):
  all green incl PINS set-eq 284/47/181/3132; RGRAM n=3132
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3133 pins" but csv + battery = 3132 (3112+20). off-by-one
  (11th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 25795 PQA, 25808 PQB, 25825/25850/25870 PQQ.
- boundaries: 25784 pinned R24 still GREEN; 25877 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 203/204 PASS-individual (w2) + cport 13 PASS-functional.
