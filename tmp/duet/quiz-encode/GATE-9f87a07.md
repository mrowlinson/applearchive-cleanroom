# GATE-9f87a07 sweep: PASS-functional (cport band24; T10R31 ->28220)

- tip: lanes/encode-cport @9f87a07 (parent merge 3dc2720 R31-partial).
  rgramc.c +550/-416: R31 16x16 76B-pay port (m-tab b37,38,72-75
  16x6B + q=_T10PWM exact @b32,33,68-71 + 62 consts), top bound 28220.
- code read (FULL): dispatch line-for-line vs w2 1912c73 (bound,
  off=n-27965, l16 2B b4,5, m/q b-sets, const loop). tables R31M
  16 EXACT; R31C 62 EXACT numeric.
- battery: legs green (RGRAM 3372, PINS set-eq 3372; C-BUILD w=0,
  all incl -C pass). HYGIENE/CONTAM/LIBCOMPRESSION FAIL =
  OBSERVED-inherited (diff rgramc.c only; same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1686/1686 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1686/1686, 3372/3372).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 27970/27990/28060/28150/28210 R31.
- boundaries: 27965 off0 + 28220 off255 py=C CLOSED; 28221 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 218/218 PASS-individual (w2) + cport 25 PASS-functional.
