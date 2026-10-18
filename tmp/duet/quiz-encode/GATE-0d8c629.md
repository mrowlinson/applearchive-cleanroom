# GATE-0d8c629 sweep: PASS-functional (cport band28; T10R34 ->29264)

- tip: lanes/encode-cport @0d8c629 (parent merge 1050d3d R34-partial).
  rgramc.c +568/-434: R34 16x16 76B-pay port (m-tab b42,43,68-71
  16x6B + q=_T10PZM exact 16x7B @b37-39,64-67 shifted footprint +
  61 consts), top bound 29264.
- code read (FULL): dispatch line-for-line vs w2 b490c4e (bound,
  off=n-29009, plain l16, m/q b-sets incl shifted q, const loop).
  tables R34M 16 EXACT; R34C 61 EXACT numeric.
- battery: legs green (RGRAM 3492, PINS set-eq 3492; C-BUILD w=0,
  all incl -C pass). HYGIENE/CONTAM/LIBCOMPRESSION FAIL =
  OBSERVED-inherited (diff rgramc.c only; same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1746/1746 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1746/1746, 3492/3492).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 29030/29060/29100/29200/29250 R34.
- boundaries: 29009 off0 + 29264 off255 py=C CLOSED; 29265 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 223/223 PASS-individual (w2) + cport 29 PASS-functional.
