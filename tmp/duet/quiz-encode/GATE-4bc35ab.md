# GATE-4bc35ab sweep: PASS-functional (cport band42; T10P440..P44Q ->32140)

- tip: lanes/encode-cport @4bc35ab (parent merge 8ac1892 P44-partial).
  rgramc.c +1068/-483: P44 5-tier port xor-lencode (P440/P441 76/76B
  + P44A 16x6B b6,7,68-71 + b5 off-set {0,9,14} + P44B 10x9B
  b6-10,72-75 + b5 off-set {1-7,9} + P44Q 4x16 P44M-16x7B b0-2,
  68-71 + P44Q-tab 4x9B b6-10,72-75 + b5-raw iff q>=1),
  top bound 32140.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 ea1b509
  (bounds 32049/32050/32066/32076/32140, offs, xor l16, b-sets;
  all 3 b5 mechanisms ternary-chains ≡ py: A {0,9,14},
  B {1,2,3,4,5,6,7,9}, Q (q>=1)). tables P44A/P44B/P44M/P44Q
  EXACT; consts 74/74/68/65/58 EXACT numeric (9/9).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3832
  + PINS-RGRAM set-eq 3832; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1916/1916 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1916/1916, 3832/3832).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, ALL THREE b5 rules BOTH ways: 32052
  A-off1 OUT, 32060 A-off9 IN, 32068 B-off1 IN, 32080 Q-off3/q0
  OUT, 32100 Q-off23/q1 IN.
- boundaries: 32049 P440 + 32140 P44Q-off63 py=C CLOSED; 32141 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 240/240 PASS-individual (w2) + cport 43 PASS-functional.
