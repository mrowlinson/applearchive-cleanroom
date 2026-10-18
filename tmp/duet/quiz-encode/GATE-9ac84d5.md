# GATE-9ac84d5 sweep: PASS-individual (rgram 3852/3852; T10R43 ->32396)

- tip: lanes/encode-writer2 @9ac84d5 (parent ea1b509 gated).
  rgram +53/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R43 16x16 76B-pay raw-lencode (off=n-32141,
  m-tab b16,17,68-71 16x6B + q=P44M split head+qtab: [:6] 3B
  @b0-2 + [6:] 4B @b64-67 + 61 consts incl b3=0x96 verified).
  AST-verified (M16 w12, P44M w14 split 6+8 consistent, C61
  sorted no-dups, const-vs-tab disjoint + FULL cover 61+13+2).
  dispatch continuous 32141->32396, no neighbor edits. for-list
  +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-9ac84d5-s12):
  all green incl OUTER2 284 + RGRAM 3852 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 32170/32230/32300/32350/32390 R43.
- boundaries: 32141 off0 + 32396 off255 CLOSED; 32397 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 240/240 PASS-individual (w2) + cport 42 PASS-functional.
