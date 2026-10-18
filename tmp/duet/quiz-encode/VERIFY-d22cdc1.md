# VERIFY-d22cdc1 merge60 P60+R59 (n<=37964): PASS

## first-hand (at-commit tree ver-d22cdc1)
- parents: 9224481 (band65) + 599f93c (R59).
- C byte-identical to band65 (cmp); py byte-identical to R59.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band65 C (n<=37616) VERIFY-9224481 GREEN; the
  P60+R59 pins 37617..37964 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
