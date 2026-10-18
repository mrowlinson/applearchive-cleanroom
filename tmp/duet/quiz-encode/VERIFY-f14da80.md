# VERIFY-f14da80 merge74 R69+P71 (n<=41472): PASS

## first-hand (at-commit tree ver-f14da80)
- parents: c0deeeb (band79) + 7fd15a0 (P71).
- C byte-identical to band79 (cmp); py byte-identical to P71.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band79 C (n<=41124) VERIFY-c0deeeb GREEN; the
  R69+P71 pins 41125..41472 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
