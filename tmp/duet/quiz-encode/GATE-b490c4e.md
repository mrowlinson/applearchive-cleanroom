# GATE-b490c4e sweep: PASS-individual (rgram 3492/3492; T10R34 ->29264)

- tip: lanes/encode-writer2 @b490c4e (parent 3dd5f7b gated).
  rgram +41/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R34 16x16 76B-pay plain-l16 (off=n-29009,
  m-tab b42,43,68-71 16x6B + q=_T10PZM exact 16x7B @b37-39,64-67
  — PZM values at shifted tail footprint vs PZQ m-tab b37-39,68-71
  — + 61 consts). AST-verified (M16 w12, C61 sorted no-dups,
  const-vs-tab disjoint + FULL cover 61+13+2). dispatch continuous
  29009->29264, no neighbor edits. for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-b490c4e-s12):
  all green incl RGRAM 3492 + PINS set-eq 3492 (tip tree). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 29030/29060/29100/29200/29250 R34.
- boundaries: 29009 off0 + 29264 off255 CLOSED; 29265 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 222/222 PASS-individual (w2) + cport 27 PASS-functional.
