# GATE-f6dfa38 sweep: PASS-individual (rgram 3652/3652; T10R38 ->30656)

- tip: lanes/encode-writer2 @f6dfa38 (parent 35d6de7 gated).
  rgram +47/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R38 16x16 76B-pay xor-lencode (off=n-30401,
  m-tab b21-23,68-71 16x7B + qhead b16,17 16x2B R38QH + qtab
  _T10P39M[q][2:] 4B @b64-67 + 61 consts). AST-verified (M16 w14,
  QH16 w4, C61 sorted no-dups, const-vs-tab disjoint + FULL cover
  61+13+2). dispatch continuous 30401->30656, no neighbor edits.
  for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-f6dfa38-s12):
  all green incl OUTER2 284 + RGRAM 3652 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 30430/30460/30520/30600/30650 R38.
- boundaries: 30401 off0 + 30656 off255 CLOSED; 30657 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 230/230 PASS-individual (w2) + cport 34 PASS-functional.
