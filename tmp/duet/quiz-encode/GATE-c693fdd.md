# GATE-c693fdd sweep: PASS-functional (cport band44; T10P450..P45Q ->32488)

- tip: lanes/encode-cport @c693fdd (parent merge 8ca0c31 P45-partial).
  rgramc.c +1071/-489: P45 5-tier port raw-lencode (P450/P451 76/76B
  + P45A 16x7B b21-23,68-71 + P45B 10x12B b13,14,20-25,72-75 +
  P45Q 4x16 P45M-16x7B b15,26,27,64-67 + P45Q-tab 4x10B b13,20-24,
  72-75 + twin head rules b14=M14[m]^(q>=2?0x04) /
  b25=M25[m]|(q>=2?0x01)), top bound 32488.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 ef80529
  (bounds 32397/32398/32414/32424/32488, offs, raw l16, b-sets;
  twin rules ^4/|1 ternary-chains ≡ py). tables P45A/P45B/P45M/
  P45Q EXACT; consts 74/74/67/62/55 EXACT numeric; M14/M25 16/16
  EXACT (11/11; first audit regex double-counted py hex — re-ran
  hex-aware, EXACT).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3872
  + PINS-RGRAM set-eq 3872; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1936/1936 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1936/1936, 3872/3872).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, q>=2-bit BOTH ways: 32406 P45A, 32420
  P45B, 32430 off5/q0 no-bit, 32450 off25/q1 no-bit, 32470 off45/q2
  bit.
- boundaries: 32397 P450 + 32488 P45Q-off63 py=C CLOSED; 32489
  rc=1 GRAMMAR-BREAK paylen 80 BOTH (this tree predates R44 +80
  gate; re-confirms 76B->80B transition + parity on errors). exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 242/242 PASS-individual (w2) + cport 45 PASS-functional.
