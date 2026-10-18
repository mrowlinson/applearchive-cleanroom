# GATE-965f4dd sweep: PASS-individual (rgram 3532/3532; T10R35 ->29612)

- tip: lanes/encode-writer2 @965f4dd (parent c108d1e gated).
  rgram +41/-0 pure addition, for-list +10 cells, pins +20 rows.
- code read (FULL): R35 16x16 76B-pay plain-l16 (off=n-29357,
  m-tab b18,19,68-71 16x6B + q=_T10P36M exact 16x6B @b13,14,64-67
  same footprint as P36Q m-tab + 62 consts). AST-verified (M16 w12,
  C62 sorted no-dups, const-vs-tab disjoint + FULL cover 62+12+2).
  dispatch continuous 29357->29612, no neighbor edits. for-list +10
  straddles edges.
- battery: all legs green EXCEPT one oracle flake (outdir
  gate-w2-965f4dd-s12): OUTER2 FAIL a-nondet "got char 14 want
  char 13" + PINS-OUTER2 FAIL rows=284 (PINSET-NEVER-PASS:a-nondet).
  cause: pin compares first-diff-char of TWO fresh AEA oracle
  encryptions — inherently nondeterministic; R35 diff is rgram-only
  and cannot influence AEA bytes. PROOF: re-ran test_outer2.sh on
  the IDENTICAL tree (outer2-rerun-r35.log) -> RC=0, PASS a-nondet,
  zero FAILs. flake documented, no FLAG (not tip-caused).
  RGRAM 3532 + PINS set-eq 3532 green on shipped run.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes: 29370/29400/29480/29550/29600 R35.
- boundaries: 29357 off0 + 29612 off255 CLOSED; 29613 rc=2 out
  of scope. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 224/224 PASS-individual (w2) + cport 29 PASS-functional.
