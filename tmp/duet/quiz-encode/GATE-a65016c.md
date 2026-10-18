# GATE-a65016c sweep: PASS-functional (cport band39; T10P420..P42Q ->31444)

- tip: lanes/encode-cport @a65016c (parent merge 23f6d99 P42-partial).
  rgramc.c +1050/-471: P42 5-tier port xor-lencode (P420/P421 76/76B
  + P42A 16x6B b16,17,68-71 + P42B 10x16B b2,12-15,17-23,72-75 +
  P42Q 4x16 P42M-16x6B b22,23,72-75 + P42Q-tab 4x9B b16-20,68-71 +
  b21 subtractive rule MB[m]-(q==1)), top bound 31444.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 a0e16b3
  (bounds 31353/31354/31370/31380/31444, offs, xor l16, b-sets;
  b21 `MB[m]-(q==1)` ≡ py incl C-bool arithmetic). tables P42A/
  P42B/P42M/P42Q EXACT; consts 74/74/68/58/58 EXACT numeric;
  MB 16 EXACT (10/10).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3752
  + PINS-RGRAM set-eq 3752; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1876/1876 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1876/1876, 3752/3752).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, b21 BOTH ways: 31362 P42A, 31376 P42B,
  31390 off9/q0 no-sub, 31400 off19/q1 sub, 31430 off49/q3 no-sub.
- boundaries: 31353 P420 + 31444 P42Q-off63 py=C CLOSED; 31445 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 236/236 PASS-individual (w2) + cport 40 PASS-functional.
