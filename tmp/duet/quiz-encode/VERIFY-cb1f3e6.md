# VERIFY-cb1f3e6 merge59 R58 (n<=37616): PASS

## first-hand (at-commit tree ver-cb1f3e6)
- parents: ae6ab12 (band64) + 9dada46 (R58).
- C byte-identical to band64 (cmp); py byte-identical to R58.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band64 C (n<=37296) VERIFY-ae6ab12 GREEN; the
  R58 pins 37297..37616 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
