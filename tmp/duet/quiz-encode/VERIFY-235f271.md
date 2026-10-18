# VERIFY-235f271 merge93 (n<=45620): PASS

## first-hand (at-commit tree v-235f271)
- parents: f341d1b (band92) + b759db1 (R81).
- C byte-identical to band92 (rgramc.c cmp); py+PINS
  byte-identical to R81 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band92 = N-list line only
  (extended thru 45620). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5486 PASS, 0 FAIL).
- C parity: band92 C (n<=45272) VERIFY-f341d1b GREEN; the
  P82+R81 pins 45273..45620 are correctly out of its scope
  (own probes w/ seat band92 bin: 45272 CLOSED T10R80B
  off=255; 45273/45620 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
