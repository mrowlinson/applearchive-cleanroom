# GATE-1b1e2f3 sweep: PASS-individual (rgram 3592/3592; T10P38 ->30052)

- tip: lanes/encode-writer2 @1b1e2f3 (parent 34f853f gated).
  rgram +201/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P38 5 tiers raw-lencode — P380/P381 singletons
  76/76B + P38A 16x7B b37-39,68-71 + P38B 10x11B b29,36-41,72-75 +
  P38Q 4x16 (P38M 16x7B b30,42,43,68-71 + P38Q-tab 4x10B b36-41,
  72-75 + NEW b29 rule: pay[29]=QB[q]+(0x40 if m>=13),
  QB=(0x12,0x16,0x26,0x12)). AST-verified (16/10/16/4, hex widths
  14/22/14/20; consts 74/74/67/63/56 sorted no-dups; const-vs-tab
  disjoint + FULL cover every tier: 67+7+2/63+11+2/56+18+2).
  dispatch continuous 29961->30052, no neighbor edits. for-list +10
  straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-1b1e2f3-s12):
  all green incl OUTER2 284 + RGRAM 3592 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes, b29 rule BOTH ways: 29970 P38A, 29984 P38B,
  29995 off6/m6 no-add, 30002 off13/m13 +0x40, 30040 off51/m3/q3.
- boundaries: 29961 P380 + 30052 P38Q-off63 CLOSED; 30053 rc=2
  out of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 227/227 PASS-individual (w2) + cport 31 PASS-functional.
