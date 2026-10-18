# GATE-cb84e10 sweep: PASS-individual (rgram 2568/2568; RANGE still HELD)

- tip: lanes/encode-writer2 @cb84e10 (parent 6e7b76a gated PASS). rgram
  +44/-0 (pure addition), for-list +6 cells, pins +12 rows append-only.
- code read (FULL, R-mirror + PAM q-reuse): T10R9 n<=20564 (20309-564,
  256 cells, follows PAQ end contiguously). m=off&15 -> R9M 16 7B
  (b25-27,64-67); q=off>>4 0..15 -> PAM[q] reuse (b20-22,60-63,
  AST-verified 16/16, q in-bounds); b5 = R9B5[q]+(q in (2,10) and
  m>=11).
- battery: GATE-PASS shipped legs (outdir gate-w2-cb84e10-s6): RGRAM
  n=2568, PINS-RGRAM set-eq 2568/2568 (6 probes incl BOTH carry-edge
  cells q2m11/q10m11 pinned ON-edge, on FRESH oracle bytes). others
  green incl OSS/LIBCOMP/ADOPT.
- storm diligence: 3 EXTRA unpinned cells ALL CLOSED rc=0: N=20351
  (q2m10, below-carry), 20479 (q10m10, below-carry), 20428 (q7m7 mid)
  — BOTH carry edges bracketed below.
- manual RED-cell re-verify @tip: N=15752 => CLOSED T9L1Q rc=0. for-
  list still LACKS 15752.
- verdict: PASS for THIS tip. FLAG-48ebfe0-hold STILL BLOCKS range
  (29 descendants, all individually-closed).
- coverage: 170/171 PASS + 1 RED-held (48ebfe0).
