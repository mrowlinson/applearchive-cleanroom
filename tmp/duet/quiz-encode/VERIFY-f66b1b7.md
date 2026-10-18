# VERIFY-f66b1b7 merge96 (n<=46664): PASS

## first-hand (at-commit tree v-f66b1b7)
- parents: 4fe183d (band95) + 7d215eb (R84).
- C byte-identical to band95 (rgramc.c cmp); py+PINS
  byte-identical to R84 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band95 = N-list line only
  (extended thru 46664). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5624 PASS, 0 FAIL).
- C parity: band95 C (n<=46316) VERIFY-4fe183d GREEN; the
  P85+R84 pins 46317..46664 are correctly out of its scope
  (own probes w/ seat band95 bin: 46316 CLOSED T10R83B
  off=255; 46317/46664 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
