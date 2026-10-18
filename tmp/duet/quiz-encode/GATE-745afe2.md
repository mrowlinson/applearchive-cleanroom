# GATE-745afe2 sweep: PASS-functional (cport band34; T10P390..P39Q ->30400)

- tip: lanes/encode-cport @745afe2 (parent merge 6a60609 P39-partial).
  rgramc.c +1032/-453: P39 5-tier port (P390 raw-lencode singleton
  quirk + P391/P39A/P39B/P39Q xor-lencode; P39A 16x7B b13-15,60-63
  + P39B 10x10B b0-2,11,16,17,72-75 + P39Q 4x16 P39M-16x5B
  b18,68-71 + P39Q-tab 4x9B b0-2,11,16,72-75 + b17 rule
  QB[q]^(m in {1-5,8,9,10} ? 0x80)), top bound 30400.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 35d6de7
  (bounds 30309/30310/30326/30336/30400, offs, P390 raw vs rest
  xor l16, b-sets; b17 ternary-chain ≡ py set; QB {78,76,79,78}
  ≡ py). tables P39A/P39B/P39M/P39Q EXACT; consts 74/74/67/64/59
  EXACT numeric; QB EXACT (10/10).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3632
  + PINS-RGRAM set-eq 3632; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1816/1816 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1816/1816, 3632/3632).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, b17 BOTH ways: 30318 P39A, 30332 P39B,
  30338 off1/m1 IN, 30343 off6/m6 OUT, 30360 off23/m7 OUT.
- boundaries: 30309 P390 + 30400 P39Q-off63 py=C CLOSED; 30401 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 230/230 PASS-individual (w2) + cport 35 PASS-functional.
