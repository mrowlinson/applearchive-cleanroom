# VERIFY-196de79 merge89 P78+R77 (n<=44228): PASS

## first-hand (at-commit tree v-196de79)
- parents: 2333b02 (band88) + e839b3d (R77).
- C byte-identical to band88 (rgramc.c/h cmp); py+PINS
  byte-identical to R77 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band88 = N-list line only
  (extended thru 44228). faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5302 pins, 0 FAIL).
- C parity: band88 C (n<=43880) VERIFY-2333b02 GREEN; the
  P78+R77 pins 43881..44228 are correctly out of its scope
  (own probes w/ seat band88 bin: 43880 CLOSED T10R76B
  off=255; 43881/44228 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
