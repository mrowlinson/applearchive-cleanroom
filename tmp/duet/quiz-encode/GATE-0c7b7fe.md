# GATE-0c7b7fe sweep: PASS-individual (rgram 3772/3772; T10R41 ->31700)

- tip: lanes/encode-writer2 @0c7b7fe (parent a0e16b3 gated).
  rgram +44/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R41 16x16 76B-pay xor-lencode (off=n-31445,
  m-tab b25-27,64-67 16x7B + qhead single byte b21 R41QH 16 ints +
  qtab _T10P42M exact 16x6B @b22,23,72-75 same footprint as P42Q
  m-tab + 60 consts). AST-verified (M16 w14, QH16, C60 sorted
  no-dups, const-vs-tab disjoint + FULL cover 60+14+2). dispatch
  continuous 31445->31700, no neighbor edits. for-list +10
  straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-0c7b7fe-s12):
  all green incl OUTER2 284 + RGRAM 3772 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 31470/31500/31560/31650/31690 R41.
- boundaries: 31445 off0 + 31700 off255 CLOSED; 31701 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 236/236 PASS-individual (w2) + cport 39 PASS-functional.
