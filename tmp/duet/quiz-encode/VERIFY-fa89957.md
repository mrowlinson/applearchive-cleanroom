# VERIFY-fa89957 merge97 (n<=47012): PASS

## first-hand (at-commit tree v-fa89957)
- parents: 0f3f997 (band96) + f418d14 (R85).
- C byte-identical to band96 (rgramc.c cmp); py+PINS
  byte-identical to R85 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band96 = N-list line only
  (extended thru 47012). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5670 PASS, 0 FAIL).
- C parity: band96 C (n<=46664) VERIFY-0f3f997 GREEN; the
  P86+R85 pins 46665..47012 are correctly out of its scope
  (own probes w/ seat band96 bin: 46664 CLOSED T10R84B
  off=255; 46665/47012 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
