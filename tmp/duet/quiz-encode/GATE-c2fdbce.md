# GATE-c2fdbce sweep: PASS-functional (cport band27; T10R33+PZ0..PZQ ->29008)

- tip: lanes/encode-cport @c2fdbce (parent merge 59cbad2 R33+P35-partial).
  rgramc.c +1138/-428: double-band port — R33 16x16 (m-tab b28-30,
  64-67 16x7B + q=PYM + 61 consts) + P35 5 tiers (PZ0/PZ1 76/76B +
  PZA 16x6B b33,34,68-71 + PZB 10x10B b25,33-37,72-75 + PZQ 4x16
  PZM-16x7B b37-39,68-71 + PZQ-tab 4x9B b28,32-35,72-75). top 29008.
- code read (FULL): all 6 dispatch blocks line-for-line vs w2
  2c07079+3dd5f7b (bounds/offs/plain-l16/b-sets). tables R33M/PZA/
  PZB/PZM/PZQ EXACT; consts 61/74/74/68/64/58 EXACT numeric (11/11).
- battery: legs green (RGRAM 3472, PINS set-eq 3472; C-BUILD w=0,
  all incl -C pass). HYGIENE/CONTAM/LIBCOMPRESSION FAIL =
  OBSERVED-inherited (diff rgramc.c only; same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1736/1736 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1736/1736, 3472/3472).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes spanning BOTH bands: 28760 R33, 28926 PZA,
  28940 PZB, 28980/29000 PZQ.
- boundaries: 28661 R33-off0 + 29008 PZQ-off63 py=C CLOSED; 29009
  rc=2 scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 222/222 PASS-individual (w2) + cport 28 PASS-functional.
