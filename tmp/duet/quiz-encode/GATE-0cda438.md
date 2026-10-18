# GATE-0cda438 sweep: PASS-individual (rgram 3692/3692; T10R39 ->31004)

- tip: lanes/encode-writer2 @0cda438 (parent 55dcb98 gated).
  rgram +41/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R39 16x16 76B-pay xor-lencode (off=n-30749,
  m-tab b37,38,68-71 16x6B + q=_T10P40M exact 16x5B @b32,64-67 —
  P40M values at shifted tail footprint vs P40Q m-tab b32,68-71 —
  + 63 consts). AST-verified (M16 w12, C63 sorted no-dups,
  const-vs-tab disjoint + FULL cover 63+11+2). dispatch continuous
  30749->31004, no neighbor edits. for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-0cda438-s12):
  all green incl OUTER2 284 + RGRAM 3692 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 30770/30800/30860/30950/30995 R39.
- boundaries: 30749 off0 + 31004 off255 CLOSED; 31005 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 232/232 PASS-individual (w2) + cport 36 PASS-functional.
