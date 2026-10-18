# GATE-b612b11 sweep: PASS-individual (rgram 2806/2806; T10P17 ->22744)

- tip: lanes/encode-writer2 @b612b11 (parent 2c562d3 gated).
  rgram +164/-0 (P17 head + PHQ), for-list +10 pure
  addition, pins +20 rows append-only.
- code read (FULL): PH0/PH1 singleton const tables
  (b5=0xb0) + PHA 16-tab 8B (b5 embedded: b5,25,46,47,
  64-67) + PHB 10-tab 9B (b2,15,45-47,68-71, sig byte
  in tab) + PHQ 4x16 (m-tab 7B b5-7,64-67 with b5
  embedded + q-tab 10B b2,3,15,45-47,68-71); NO b5 rule
  anywhere — b5 carried in PHA/PHM tabs (PHQ branch has
  mtab+qtab+const only, read first-hand). table counts
  AST-verified (16/10/16/4, widths 16/18/14/20 hex).
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-b612b11-s9):
  RGRAM n=2806, PINS-RGRAM set-eq 2806/2806, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 22656 (PHA off1), 22675 (PHB off4),
  22690 (PHQ off9), 22710 (PHQ off29), 22730 (PHQ off49).
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 184/185 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
