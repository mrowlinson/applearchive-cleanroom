# VERIFY-ea54647 merge88 P77+R76 (n<=43880): PASS

## first-hand (at-commit tree v-ea54647)
- parents: d68dbff (band87) + 795f3f8 (R76).
- C byte-identical to band87 (rgramc.c/h cmp); py+PINS
  byte-identical to R76 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band87 = N-list line only
  (extended thru 43880). faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5256 pins, 0 FAIL).
- C parity: band87 C (n<=43532) VERIFY-d68dbff GREEN; the
  P77+R76 pins 43533..43880 are correctly out of its scope
  (own probes w/ seat band87 bin: 43532 CLOSED T10R75B
  off=255; 43533/43880 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
