# GATE-497b4f4 sweep: PASS-individual (rgram 3732/3732; T10R40 ->31352)

- tip: lanes/encode-writer2 @497b4f4 (parent 47eb5fa gated).
  rgram +43/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R40 16x16 76B-pay raw-lencode swapped (off=n-31097,
  b5-qbit set {0,1,6,8,9} — same set as P41Q m-set, swapped axis
  like R32/PXQ — m-tab b0,1,11,68-71 16x7B b0-tabbed + q=_T10P41M
  exact 16x6B @b6,7,64-67 shifted vs P41Q m-tab b6,7,68-71 + 61
  consts). AST-verified (M16 w14, C61 sorted no-dups, const-vs-tab
  disjoint + FULL cover 61+13+2). dispatch continuous 31097->31352,
  no neighbor edits. for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-497b4f4-s12):
  all green incl OUTER2 284 + RGRAM 3732 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b5-qbit BOTH ways: 31100 q0 IN, 31135 off38/q2
  OUT, 31200 off103/q6 IN, 31220 off123/q7 OUT, 31300 off203/q12 OUT.
- boundaries: 31097 off0 + 31352 off255 CLOSED; 31353 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 234/234 PASS-individual (w2) + cport 37 PASS-functional.
