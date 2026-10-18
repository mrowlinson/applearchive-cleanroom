# VERIFY-8233b06 merge94 (n<=45968): PASS

## first-hand (at-commit tree v-8233b06)
- parents: 43b0519 (band93) + fd558ad (R82).
- C byte-identical to band93 (rgramc.c cmp); py+PINS
  byte-identical to R82 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band93 = N-list line only
  (extended thru 45968). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5532 PASS, 0 FAIL).
- C parity: band93 C (n<=45620) VERIFY-43b0519 GREEN; the
  P83+R82 pins 45621..45968 are correctly out of its scope
  (own probes w/ seat band93 bin: 45620 CLOSED T10R81B
  off=255; 45621/45968 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
