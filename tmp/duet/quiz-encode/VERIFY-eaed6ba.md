# VERIFY-eaed6ba merge57 P58 (n<=36948): PASS

## first-hand (at-commit tree ver-eaed6ba)
- parents: 6a04351 (band62) + 1165cfa (P58).
- C byte-identical to band62 (cmp); py byte-identical to P58.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band62 C (n<=36920) VERIFY-6a04351 GREEN; the
  P58 pins 36921..36948 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
