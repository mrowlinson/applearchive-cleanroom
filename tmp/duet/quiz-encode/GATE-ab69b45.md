# GATE-ab69b45 sweep: PASS-functional (cport band38; T10R40 ->31352)

- tip: lanes/encode-cport @ab69b45 (parent merge ebd77e1 R40-partial).
  rgramc.c +606/-470: R40 16x16 76B-pay port raw-lencode (b5-qbit
  set {0,1,6,8,9}, m-tab b0,1,11,68-71 16x7B + q=P41M exact 16x6B
  @b6,7,64-67 + 61 consts), top bound 31352.
- code read (FULL): dispatch line-for-line vs w2 497b4f4 (bound,
  off=n-31097, raw lencode both bytes, q-set ternary-chain ≡ py,
  m/q b-sets, const loop). tables R40M 16 EXACT; R40C 61 EXACT
  numeric.
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3732
  + PINS-RGRAM set-eq 3732; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1866/1866 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1866/1866, 3732/3732).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes, b5-qbit BOTH ways: 31100 q0 IN, 31135
  off38/q2 OUT, 31200 off103/q6 IN, 31220 off123/q7 OUT, 31300
  off203/q12 OUT.
- boundaries: 31097 off0 + 31352 off255 py=C CLOSED; 31353 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 235/235 PASS-individual (w2) + cport 39 PASS-functional.
