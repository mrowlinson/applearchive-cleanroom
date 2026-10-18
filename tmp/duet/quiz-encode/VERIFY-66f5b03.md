# VERIFY-66f5b03 merge61 P61 (n<=37992): PASS

## first-hand (at-commit tree ver-66f5b03)
- parents: a07ce91 (band66) + 5a8e107 (P61).
- C byte-identical to band66 (cmp); py byte-identical to P61.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band66 C (n<=37964) VERIFY-a07ce91 GREEN; the
  P61 pins 37965..37992 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
