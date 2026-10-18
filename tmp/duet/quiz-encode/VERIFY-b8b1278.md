# VERIFY-b8b1278 merge-R73 (n<=42836): PASS

## first-hand (at-commit tree v-b8b1278)
- parents: b6151b1 (band84) + 93098c6 (R73).
- C byte-identical to band84 (rgramc.c/h cmp); py+PINS
  byte-identical to R73 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band84 = N-list line only
  (extended thru 42836). faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5118 pins, 0 FAIL).
- C parity: band84 C (n<=42516) VERIFY-b6151b1 GREEN; the
  R73 pins 42517..42836 are correctly out of its scope
  (own probes w/ seat band84 bin: 42516 CLOSED T10P74B
  off=9; 42517/42836 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
