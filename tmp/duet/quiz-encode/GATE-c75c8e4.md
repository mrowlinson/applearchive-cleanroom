# GATE-c75c8e4 sweep: PASS-individual (rgram 2750/2750; T10R14 22049..22304)

- tip: lanes/encode-writer2 @c75c8e4 (parent 6940ea2 gated).
  rgram +42/-0 (T10R14 branch + tables), for-list +8 pure
  addition, pins +16 rows append-only.
- code read (FULL): _T10R14M 16 lits (m-tab 7B
  b20-22,56-59, AST-verified) + _T10R14C consts; b5 rule
  0xac+(off>=95)+(off>=223) dbl-carry; q-tab 6B reuses
  _T10PFM[q]. carry edges in for-list: 22143/22144
  (off94/95 ac->ad), 22271/22272 (off222/223 ad->ae).
  pure addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-c75c8e4-s9):
  RGRAM n=2750, PINS-RGRAM set-eq 2750/2750, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 22050 (off1), 22142 (off93, ac
  side), 22145 (off96, ad side), 22270 (off221, ad side),
  22273 (off224, ae side) — both carry edges covered
  both ways.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 181/182 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
