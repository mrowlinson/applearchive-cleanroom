# GATE-8da8428 sweep: PASS-individual (rgram 3392/3392; T10P33 ->28312)

- tip: lanes/encode-writer2 @8da8428 (parent 1912c73 gated).
  rgram +201/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): P33 5 tiers — PX0/PX1 singletons 76/76B +
  PXA 16x7B b29,46,47,68-71 + PXB 10x11B b0,1,26,27,45-47,72-75
  (b0-tabbed) + PXQ 4x16 (PXM 16x5B b6,72-75 + PXQ-tab 4x10B
  b1,26,27,45-47,68-71; b5-mbit rule m in {0-4,6,12,14} xor 0x80).
  AST-verified (16/10/16/4, hex widths 14/22/10/20; consts
  74/74/67/63/59 sorted no-dups; const-vs-tab disjoint + FULL
  cover every tier). dispatch continuous 28221->28312, no neighbor
  edits. for-list +10 straddles all edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-8da8428-s12):
  all green incl RGRAM 3392 + PINS set-eq 3392 (tip tree). no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 28230 PXA, 28244 PXB, 28255/28290/28305 PXQ.
- boundaries: 28221 PX0 + 28312 PXQ-off63 CLOSED; 28313 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 217/217 PASS-individual (w2) + cport 24 PASS-functional.
