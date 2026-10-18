# GATE-074bf0a sweep: PASS-individual (rgram 3892/3892; T10R44 ->32744)

- tip: lanes/encode-writer2 @074bf0a (parent ef80529 gated).
  rgram +58/-1 (gate-line +80 + R44 block), for-list +10, pins +20.
- code read (FULL): R44 FIRST 80B tier (off=n-32489, raw lencode,
  m-tab b36,72-75 16x5B + qhead b18,19,29 16x3B R44QH + qtab
  _T10P45M[q][2:] 6B @b30,31,68-71 + 64 consts). AST-verified
  over range(80) (M16 w10, QH16 w6, C64 sorted no-dups maxb 79,
  const-vs-tab disjoint + FULL cover 64+14+2). 3 hunks only:
  tables insert + paylen gate +80 + dispatch append; NO neighbor
  edits. dispatch continuous 32489->32744. for-list +10 straddles
  edges. paylen-gate edit CONFIRMS P45 GATE regime-transition call.
- battery: GATE-PASS shipped legs (outdir gate-w2-074bf0a-s12):
  all green incl OUTER2 284 + RGRAM 3892 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 32510/32580/32650/32700/32740 R44.
- boundaries: 32489 off0 + 32744 off255 CLOSED; 32745 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 242/242 PASS-individual (w2) + cport 44 PASS-functional.
