# GATE-1cc206b sweep: PASS-functional (cport band22; T10R30 ->27872)

- tip: lanes/encode-cport @1cc206b (parent merge f1ffe3c R30-partial).
  rgramc.c +571/-410: R30 16x16 76B-pay port (m-tab b21,22,72-75 16x6B
  + qhead b17,18 16x2B + qtab PVM-suf+4 + 62 consts), top bound 27872.
- code read (FULL): dispatch line-for-line vs w2 8e0d740 (off/m/q, l16
  2B b4,5, b-sets, PVM[q]+4 == [4:], const loop). tables R30M/R30QH
  16/16 EXACT; R30C 62/62 numeric-EXACT (9 rows C drops leading zero:
  '0a' vs 'a' etc, values equal). top-bound R30, 192 CLOSED tags.
- battery: legs green (RGRAM 3332, PINS set-eq 3332; C-BUILD w=0,
  all RAWENC/PBZE/LZMA/LZ4/SMOKE/UNITS incl -C pass).
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL = OBSERVED-inherited (diff
  touches rgramc.c only; same-cause per 032/033, no FLAG).
- parity: RGRAMC-PYID 1666/1666 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1666/1666, 3332/3332).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 27625/27640/27660/27690/27750 R30.
- boundaries: 27617 off0 + 27872 off255 py=C CLOSED; 27873 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 215/216 PASS-individual (w2) + cport 23 PASS-functional.
