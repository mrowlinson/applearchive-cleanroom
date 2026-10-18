# GATE-47eb5fa sweep: PASS-individual (rgram 3712/3712; T10P41 ->31096)

- tip: lanes/encode-writer2 @47eb5fa (parent 0cda438 gated).
  rgram +201/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P41 5 tiers xor-lencode — P410/P411 singletons
  76/76B + P41A 16x6B b42,43,68-71 + P41B 10x11B b15,29-31,41-43,
  72-75 + P41Q 4x16 (P41M 16x6B b6,7,68-71 + P41Q-tab 4x9B
  b30,31,41-43,72-75 + b5 m-bit: pay[4] vs xor-low BUT pay[5] vs
  RAW-high ^ (0x80 if m in {0,1,6,8,9}) — mixed-base b5).
  AST-verified (16/10/16/4, hex widths 12/22/12/18; consts
  74/74/68/63/59 sorted no-dups; const-vs-tab disjoint + FULL
  cover every tier: 68+6+2/63+11+2/59+15+2). dispatch continuous
  31005->31096, no neighbor edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-47eb5fa-s12):
  all green incl OUTER2 284 + RGRAM 3712 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b5 set BOTH ways: 31014 P41A, 31028 P41B,
  31034 off1/m1 IN, 31035 off2/m2 OUT, 31060 off27/m11 OUT.
- boundaries: 31005 P410 + 31096 P41Q-off63 CLOSED; 31097 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 233/233 PASS-individual (w2) + cport 36 PASS-functional.
