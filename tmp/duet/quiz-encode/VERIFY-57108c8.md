# VERIFY-57108c8 merge62 R60+P62 (n<=38340): PASS

## first-hand (at-commit tree ver-57108c8)
- parents: 17a2872 (band67) + 3917ba1 (P62).
- C byte-identical to band67 (cmp); py byte-identical to P62.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band67 C (n<=37992) VERIFY-17a2872 GREEN; the
  R60+P62 pins 37993..38340 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
