# VERIFY-234bf1b merge95 (n<=46316): PASS

## first-hand (at-commit tree v-234bf1b)
- parents: fecaa3d (band94) + e0b4455 (R83).
- C byte-identical to band94 (rgramc.c cmp); py+PINS
  byte-identical to R83 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band94 = N-list line only
  (extended thru 46316). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5578 PASS, 0 FAIL).
- C parity: band94 C (n<=45968) VERIFY-fecaa3d GREEN; the
  P84+R83 pins 45969..46316 are correctly out of its scope
  (own probes w/ seat band94 bin: 45968 CLOSED T10R82B
  off=255; 45969/46316 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
