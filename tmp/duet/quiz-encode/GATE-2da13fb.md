# GATE-2da13fb sweep: PASS-individual (rgram 2694/2694; T10P14 ->21700)

- tip: lanes/encode-writer2 @2da13fb (parent 5d1715c gated).
  rgram +165/-0 (P14 head + PEQ), for-list +10 pure
  addition, pins +20 rows append-only.
- code read (FULL): PE0/PE1 singleton const tables (b5=0x28)
  + PEA 16-tab 5B (b37,64-67) + PEB 10-tab 10B (b5
  embedded, b5,40-44,68-71) + PEQ 4x16 (m-tab 6B
  b45,46,68-71 + q-tab 8B b40-43,64-67); NO b5 rule —
  const 0x28 head / 0x29 PEQ via const tables (PEQ branch
  has mtab+qtab+const only, read first-hand). table counts
  AST-verified (16/10/16/4, widths 10/20/12/16 hex).
  head split 21631/21632 (PEB off4/off5) in storm below.
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-2da13fb-s9):
  RGRAM n=2694, PINS-RGRAM set-eq 2694/2694, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 21612 (PEA off1), 21631 (PEB off4,
  0x28 side), 21632 (PEB off5, 0x29 side), 21645 (PEQ
  m8q0), 21680 (PEQ m11q2).
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 178/179 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
