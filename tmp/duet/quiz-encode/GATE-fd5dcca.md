# GATE-fd5dcca sweep: PASS-functional (cport band33; T10R37 ->30308)

- tip: lanes/encode-cport @fd5dcca (parent merge 0a99a6e R37-partial).
  rgramc.c +615/-452: R37 16x16 76B-pay port raw-lencode (b5 m-bit
  set {0,1,9,10,11,12,13,14}, m-tab b6,7,68-71 16x6B + qhead
  b29,30 16x2B R37QH + qtab P38M-tail [2:] 6B @b42,43,64-67 +
  60 consts), top bound 30308.
- code read (FULL): dispatch line-for-line vs w2 b1f4334 (bound,
  off=n-30053, raw l16, b5 ternary-chain ≡ py set, m/qhead/qtab
  b-sets, suffix +(2) ≡ [2:], const loop). tables R37M/R37QH
  16/16 EXACT; R37C 60 EXACT numeric.
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3612
  + PINS-RGRAM set-eq 3612; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1806/1806 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1806/1806, 3612/3612).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, b5 set BOTH ways: 30054 m1 IN, 30055 m2
  OUT, 30062 m9 IN, 30150 off97/m1 IN, 30200 off147/m3 OUT.
- boundaries: 30053 off0 + 30308 off255 py=C CLOSED; 30309 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 229/229 PASS-individual (w2) + cport 34 PASS-functional.
