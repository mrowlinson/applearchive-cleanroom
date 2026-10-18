# GATE-1b84bca sweep: PASS-functional (cport band40; T10R41 ->31700)

- tip: lanes/encode-cport @1b84bca (parent merge 8b8a699 R41-partial).
  rgramc.c +613/-476: R41 16x16 76B-pay port xor-lencode (m-tab
  b25-27,64-67 16x7B + qhead single byte b21 R41QH 16 ints + qtab
  P42M exact 16x6B @b22,23,72-75 + 60 consts), top bound 31700.
- code read (FULL): dispatch line-for-line vs w2 0c7b7fe (bound,
  off=n-31445, xor l16, m/qhead/qtab b-sets, single-byte qhead
  compare, const loop). tables R41M 16 EXACT; R41QH 16 EXACT;
  R41C 60 EXACT numeric.
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3772
  + PINS-RGRAM set-eq 3772; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1886/1886 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1886/1886, 3772/3772).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 31470/31500/31560/31650/31690 R41.
- boundaries: 31445 off0 + 31700 off255 py=C CLOSED; 31701 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 238/238 PASS-individual (w2) + cport 41 PASS-functional.
