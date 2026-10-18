# GATE-5d1715c sweep: PASS-individual (rgram 2674/2674; T10R12 21353..21608)

- tip: lanes/encode-writer2 @5d1715c (parent 30a6964 gated).
  rgram +44/-0 (T10R12 branch + tables), for-list +8 pure
  addition, pins +16 rows append-only.
- code read (FULL): _T10R12M 16 lits (m-tab 6B
  b33,34,64-67) + _T10R12B5 ramp 0x26x2/0x27x8/0x28x6
  (AST-verified exact) + _T10R12C consts; b5 rule
  B5[q]+(q in (1,9) and m>=7); q-tab 6B reuses _T10PDM[q].
  carry edges in for-list: 21375/21376 (q1 m6/m7),
  21503/21504 (q9 m6/m7) + m0 anchors 21369/21497.
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-5d1715c-s9):
  RGRAM n=2674, PINS-RGRAM set-eq 2674/2674, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 21354 (m1q0), 21374 (m5q1, 0x26
  side), 21377 (m8q1, 0x27 side), 21502 (m5q9, 0x27
  side), 21505 (m8q9, 0x28 side) — both carry edges
  covered both ways.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 177/178 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
