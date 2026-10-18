# VERIFY-97e5ee8 merge69 R65+P67 (n<=40080): PASS

## first-hand (at-commit tree ver-97e5ee8)
- parents: 2a2f2b7 (band74) + 1030015 (P67).
- C byte-identical to band74 (cmp); py byte-identical to P67.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band74 C (n<=39732) VERIFY-2a2f2b7 GREEN; the
  R65+P67 pins 39733..40080 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
