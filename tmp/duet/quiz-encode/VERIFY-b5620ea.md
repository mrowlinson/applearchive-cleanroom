# VERIFY-b5620ea merge83 P73 (n<=42168): PASS

## first-hand (at-commit tree v-b5620ea)
- parents: 7c309fc (band82) + 312aa28 (P73).
- C byte-identical to band82 (rgramc.c/h cmp); py+PINS
  byte-identical to P73 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh = band82 script (RGRAM_BIN hook kept)
  + P73 N-list tail (42141..42168 Ns); otherwise ident to
  both parents' logic. faithful partial-merge shape.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN
  (5046 pins, 0 FAIL).
- C parity: band82 C (n<=42140) VERIFY-7c309fc GREEN; the
  P73 pins 42141..42168 are correctly out of its scope
  (own probes w/ seat band82 bin: 42140 CLOSED T10R71B
  off=255; 42141/42154/42168 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b.

## verdict: PASS (faithful merge, no skew)
