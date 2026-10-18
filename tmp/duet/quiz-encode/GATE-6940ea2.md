# GATE-6940ea2 sweep: PASS-individual (rgram 2734/2734; T10P15 ->22048)

- tip: lanes/encode-writer2 @6940ea2 (parent 55fcd0d gated).
  rgram +166/-0 (P15 head + PFQ), for-list +10 pure
  addition, pins +20 rows append-only.
- code read (FULL): PF0/PF1 singleton const tables
  (b5=0x2b/0xab) + PFA 16-tab 6B (b0,11,64-67) + PFB
  10-tab 9B (b0,1,11-13,68-71) + PFQ 4x16 (m-tab 6B
  b16,17,68-71 + q-tab 9B b0,1,11-13,64-67); PFQ b5
  rule 0xab+(off>=31); head const 0xab. table counts
  AST-verified (16/10/16/4, widths 12/18/12/18 hex).
  b5 edge pair in for-list: 22015 (off30=0xab) /
  22016 (off31=0xac). pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-6940ea2-s9):
  RGRAM n=2734, PINS-RGRAM set-eq 2734/2734, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 21960 (PFA off1), 21980 (PFB off5),
  21995 (PFQ off10, 0xab side), 22014 (off29, 0xab side),
  22017 (off32, 0xac side) — b5 edge covered both ways.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 180/181 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
