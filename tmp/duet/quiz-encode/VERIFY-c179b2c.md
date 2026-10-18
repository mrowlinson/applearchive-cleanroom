# VERIFY-c179b2c merge87 P76+R75 (n<=43532): PASS

## first-hand (at-commit tree v-c179b2c)
- parents: ead5f7c (band86) + 365b4b2 (R75).
- C byte-identical to band86 (rgramc.c/h cmp); py+PINS
  byte-identical to R75 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band86 = N-list line only
  (extended thru 43532). faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5210 pins, 0 FAIL).
- C parity: band86 C (n<=43184) VERIFY-ead5f7c GREEN; the
  P76+R75 pins 43185..43532 are correctly out of its scope
  (own probes w/ seat band86 bin: 43184 CLOSED T10R74B
  off=255; 43185/43532 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
