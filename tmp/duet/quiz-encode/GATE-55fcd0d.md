# GATE-55fcd0d sweep: PASS-individual (rgram 2714/2714; T10R13 21701..21956)

- tip: lanes/encode-writer2 @55fcd0d (parent 2da13fb gated).
  rgram +47/-0 (T10R13 branch + tables), for-list +10 pure
  addition, pins +20 rows append-only.
- code read (FULL): _T10R13M 16 lits (m-tab 6B
  b6,7,48-51) + _T10R13B5 ramp 0x29x4/0x2ax8/0x2bx4
  (AST-verified exact) + _T10R13C consts; b5 rule
  B5[q]+(q in (3,11) and m>=11) then |=0x80 iff m in
  (1,2,3,8) — flip+spike; q-tab 6B reuses _T10PEM[q].
  carry edges in for-list: 21759/21760 (q3 m10/m11),
  21887/21888 (q11 m10/m11) + spike samples 21702 (m1),
  21709 (m8), 21750 (m1q3), 21885 (m8q11). pure
  addition, no neighbor edits.
- battery: GATE-PASS shipped legs (outdir gate-w2-55fcd0d-s9):
  RGRAM n=2714, PINS-RGRAM set-eq 2714/2714, all others
  green incl HYGIENE/CONTAM/OSS/LIBCOMPRESSION/ADOPT.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 21703 (m2q0 spike), 21758 (m9q3,
  0x29 no-spike), 21761 (m12q3, 0x2a carry), 21886
  (m9q11, 0x2a no-spike), 21889 (m13q11, 0x2b carry) —
  both carry edges + spike/non-spike covered.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 179/180 PASS-individual + 1 RED-cleared.
  ZERO holds vs NOTE-092 baseline.
