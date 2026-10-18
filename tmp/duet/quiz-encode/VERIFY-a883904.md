# VERIFY-a883904 merge91 (n<=44924): PASS

## first-hand (at-commit tree v-a883904)
- parents: a735473 (band90) + 4a40af9 (R79).
- C byte-identical to band90 (rgramc.c/h cmp); py+PINS
  byte-identical to R79 (rgram.py, rgram-PINS.csv cmp).
- tests/test_rgram.sh diff vs band90 = N-list line only
  (extended thru 44924). faithful partial-merge shape.
- `tests/test_rgram.sh` own run: RGRAM-GREEN
  (5394 PASS, 0 FAIL).
- C parity: band90 C (n<=44576) VERIFY-a735473 GREEN; the
  P80+R79 pins 44577..44924 are correctly out of its scope
  (own probes w/ seat band90 bin: 44576 CLOSED T10R78B
  off=255; 44577/44924 rc=2 "N out of scope").
  RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-3367c4b.

## verdict: PASS (faithful merge, no skew)
