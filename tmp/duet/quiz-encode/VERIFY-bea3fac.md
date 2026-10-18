# VERIFY-bea3fac merge84 R72+P74 (n<=42516): PASS

## first-hand (at-commit tree v-bea3fac)
- parents: de31018 (band83) + 9fb2c01 (P74).
- C byte-identical to band83 (rgramc.c/h cmp); py+PINS
  byte-identical to P74 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh = band83 script (RGRAM_BIN hook kept)
  + N-list tail extended thru 42516 (R72+P74 Ns).
  faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5092 pins, 0 FAIL).
- C parity: band83 C (n<=42168) VERIFY-de31018 GREEN; the
  R72+P74 pins 42169..42516 are correctly out of its scope
  (own probes w/ seat band83 bin: 42168 CLOSED T10P73B
  off=9; 42169/42489/42516 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
