# GATE-9783bf5 sweep: PASS-individual (rgram 3096/3096; T10P25 ->25528)

- tip: lanes/encode-writer2 @9783bf5 (parent d3afa19 gated).
  rgram +168/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): PP0/PP1 singletons (72/76B) + PPA 16x6B
  b50,51,68-71 + PPB 10x9B b30,31,49-51,72-75 + PPQ 4x16 76B
  (PPM 16x6B b6,7,72-75 + PPQ-tab 4x9B b30,31,49-51,68-71 +
  b5 PPB5[m]-(off<7) mtab). counts AST-verified (71/75/16/69/
  10/66/16/4/16/59; hex widths 12/18/12/18; const idx sorted,
  no dups). const-vs-tab disjoint + FULL cover every tier
  (71+1/75+1/69+6+1/66+9+1/59+6+9+1+1). dispatch continuous
  25436->25528, no neighbor edits. for-list straddles b5 edge
  off6/7 + all tier edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-9783bf5-s12):
  all green incl PINS set-eq 284/47/181/3096; RGRAM n=3096
  rc=0 zero FAIL (tip tree, NVME workdir). no flake.
- observation (message slip, no functional impact): msg claims
  "3097 pins" but csv + battery = 3096 (3076+20). off-by-one
  (9th in series).
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 25445 PPA, 25460 PPB, 25480/25500/25520 PPQ.
- boundaries: 25436 pinned R23 still GREEN; 25529 rc=2 out of
  scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 201/202 PASS-individual (w2) + cport 0/11-held.
