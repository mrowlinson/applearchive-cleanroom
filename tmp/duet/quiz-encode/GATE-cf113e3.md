# GATE-cf113e3 sweep: PASS-individual (rgram 3812/3812; T10R42 ->32048)

- tip: lanes/encode-writer2 @cf113e3 (parent 25b36b0 gated).
  rgram +46/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R42 16x16 76B-pay xor-lencode (off=n-31793,
  m-tab b33,42,43,64-67 16x7B + qhead b36-38 16x3B R42QH + qtab
  _T10P43M[q][6:] 4B @b72-75 + 60 consts). AST-verified (M16 w14,
  QH16 w6, C60 sorted no-dups, const-vs-tab disjoint + FULL cover
  60+14+2). MESSAGE SLIP (loud): commit msg claims "m-tab b0,1,2
  row-mid" but CODE tabs b33,42,43,64-67 and b0/1/2 are CONSTS
  (verified in R42C). code self-consistent + battery green, so
  PASS on code truth; msg prose wrong. dispatch continuous
  31793->32048, no neighbor edits. for-list +10 straddles edges.
- battery: GATE-PASS shipped legs (outdir gate-w2-cf113e3-s12):
  all green incl OUTER2 284 + RGRAM 3812 + PINS set-eq (tip tree).
  no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 31820/31850/31910/32000/32040 R42.
- boundaries: 31793 off0 + 32048 off255 CLOSED; 32049 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 238/238 PASS-individual (w2) + cport 40 PASS-functional.
