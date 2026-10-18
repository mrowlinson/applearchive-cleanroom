# GATE-9126bc1 sweep: PASS-individual (rgram 2622/2622; T10P12 ->21004)

- tip: lanes/encode-writer2 @9126bc1 (parent 68ff2b4 gated).
  rgram +167/-0 (P12 head + PCQ), for-list +10 pure
  addition, pins +20 rows append-only.
- code read (FULL): PC0/PC1 singleton const tables + PCA
  16-tab 7B (b5-7,56-59) + PCB 10-tab 10B (b5-10,68-71) +
  PCQ 4x16 (m-tab 7B b0,1,11,68-71 + q-tab 9B b6-10,
  64-67) + _T10PCQ5 (23,23,a3,24) with b5 rule PCQ5[q] -
  (q==3 and m<3); dispatch chain PC0/PC1/PCA/PCB/PCQ.
  table counts AST-verified (16/10/16/4/4). b5 edge pair
  in for-list: 20991 (m2q3=0x23) / 20992 (m3q3=0x24).
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-9126bc1-s9):
  RGRAM n=2622, PINS-RGRAM set-eq 2622/2622, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 20916 (PCA off1), 20935 (PCB off4),
  20950 (PCQ m9q0), 20990 (m1q3, b5=0x23 side),
  20993 (m4q3, b5=0x24 side) — b5 edge covered both ways.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 174/175 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
