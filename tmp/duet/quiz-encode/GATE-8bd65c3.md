# GATE-8bd65c3 sweep: PASS-functional (cport band35; T10R38 ->30656)

- tip: lanes/encode-cport @8bd65c3 (parent merge 968244b R38-partial).
  rgramc.c +618/-458: R38 16x16 76B-pay port xor-lencode (m-tab
  b21-23,68-71 16x7B + qhead b16,17 16x2B R38QH + qtab P39M-tail
  [2:] 4B @b64-67 + 61 consts), top bound 30656.
- code read (FULL): dispatch line-for-line vs w2 f6dfa38 (bound,
  off=n-30401, xor l16, m/qhead/qtab b-sets, suffix +(2) ≡ [2:],
  const loop). tables R38M/R38QH 16/16 EXACT; R38C 61 EXACT numeric.
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3652
  + PINS-RGRAM set-eq 3652; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1826/1826 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1826/1826, 3652/3652).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 30430/30460/30520/30600/30650 R38.
- boundaries: 30401 off0 + 30656 off255 py=C CLOSED; 30657 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 231/231 PASS-individual (w2) + cport 36 PASS-functional.
