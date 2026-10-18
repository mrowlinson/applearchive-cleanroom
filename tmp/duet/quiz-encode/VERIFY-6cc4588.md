# VERIFY-6cc4588 merge92 (n<=45272): PASS

## first-hand (at-commit tree v-6cc4588)
- parents: 98b271f (band91) + 2ebec70 (R80).
- C byte-identical to band91 (rgramc.c/h cmp); py+PINS
  byte-identical to R80 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band91 = N-list line only
  (extended thru 45272). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5440 PASS, 0 FAIL).
- C parity: band91 C (n<=44924) VERIFY-98b271f GREEN; the
  P81+R80 pins 44925..45272 are correctly out of its scope
  (own probes w/ seat band91 bin: 44924 CLOSED T10R79B
  off=255; 44925/45272 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
