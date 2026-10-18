# VERIFY-7d2affe merge71 R67 (n<=40748): PASS

## first-hand (at-commit tree ver-7d2affe)
- parents: 9570115 (band76) + c55aa3c (R67).
- C byte-identical to band76 (cmp); py byte-identical to R67.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band76 C (n<=40428) VERIFY-9570115 GREEN; the
  R67 pins 40429..40748 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
