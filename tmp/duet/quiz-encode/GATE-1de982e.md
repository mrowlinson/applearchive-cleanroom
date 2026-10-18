# GATE-1de982e sweep: PASS-functional (cport band30; T10R35 ->29612)

- tip: lanes/encode-cport @1de982e (parent merge 6abb47e R35-partial).
  rgramc.c +574/-440: R35 16x16 76B-pay port (m-tab b18,19,68-71
  16x6B + q=_T10P36M exact 16x6B @b13,14,64-67 + 62 consts),
  top bound 29612.
- code read (FULL): dispatch line-for-line vs w2 965f4dd (bound,
  off=n-29357, plain l16, m/q b-sets, const loop). tables R35M
  16 EXACT; R35C 62 EXACT numeric.
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3532
  + PINS-RGRAM set-eq 3532; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1766/1766 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1766/1766, 3532/3532).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 29370/29400/29480/29550/29600 R35.
- boundaries: 29357 off0 + 29612 off255 py=C CLOSED; 29613 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 225/225 PASS-individual (w2) + cport 31 PASS-functional.
