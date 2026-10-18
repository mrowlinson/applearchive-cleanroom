# GATE-34f853f sweep: PASS-individual (rgram 3572/3572; T10R36 ->29960)

- tip: lanes/encode-writer2 @34f853f (parent f43ec6a gated).
  rgram +51/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R36 16x16 76B-pay raw-lencode (off=n-29705,
  m-tab b32-34,68-71 16x7B + qhead b14,15,25-27 16x5B R36QH +
  qtab _T10P37M[q][6:] 4B @b64-67 + 58 consts). AST-verified (M16
  w14, QH16 w10, C58 sorted no-dups, const-vs-tab disjoint + FULL
  cover 58+16+2). dispatch continuous 29705->29960, no neighbor
  edits. for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-34f853f-s12):
  all green incl OUTER2 284 + RGRAM 3572 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 29730/29760/29820/29900/29950 R36.
- boundaries: 29705 off0 + 29960 off255 CLOSED; 29961 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 226/226 PASS-individual (w2) + cport 31 PASS-functional.
