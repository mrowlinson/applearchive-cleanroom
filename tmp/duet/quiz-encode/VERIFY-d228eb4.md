# VERIFY-d228eb4 merge58 R57+P59 (n<=37296): PASS

## first-hand (at-commit tree ver-d228eb4)
- parents: f8fc439 (band63) + 36d0b16 (P59).
- C byte-identical to band63 (cmp); py byte-identical to P59.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band63 C (n<=36948) VERIFY-f8fc439 GREEN; the
  R57+P59 pins 36949..37296 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
