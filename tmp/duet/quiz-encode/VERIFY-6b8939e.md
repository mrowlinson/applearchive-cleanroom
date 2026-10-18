# VERIFY-6b8939e merge56 P57+R56 (n<=36920): PASS

## first-hand (at-commit tree ver-6b8939e)
- parents: 42b1e16 (band61) + 3dfc862 (R56).
- C byte-identical to band61 (cmp); py byte-identical to R56.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band61 C (n<=36572) VERIFY-42b1e16 GREEN; the
  P57+R56 pins 36573..36920 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
