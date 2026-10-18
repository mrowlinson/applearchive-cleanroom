# VERIFY-dc6552e merge63 R61 (n<=38660): PASS

## first-hand (at-commit tree ver-dc6552e)
- parents: cac2faf (band68) + e2f8de7 (R61).
- C byte-identical to band68 (cmp); py byte-identical to R61.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band68 C (n<=38340) VERIFY-cac2faf GREEN; the
  R61 pins 38341..38660 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
