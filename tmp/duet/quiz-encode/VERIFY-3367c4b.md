# VERIFY-3367c4b merge90 (n<=44576): PASS

## first-hand (at-commit tree v-3367c4b)
- parents: a6e4edc (band89) + 3a0891e (R78).
- C byte-identical to band89 (rgramc.c/h cmp); py+PINS
  byte-identical to R78 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band89 = N-list line only
  (extended thru 44576). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5348 PASS, 0 FAIL).
- C parity: band89 C (n<=44228) VERIFY-a6e4edc GREEN; the
  P79+R78 pins 44229..44576 are correctly out of its scope
  (own probes w/ seat band89 bin: 44228 CLOSED T10R77B
  off=255; 44229/44576 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-b8b1278.

## verdict: PASS (faithful merge, no skew)
