# VERIFY-4b3e3e8 merge66 R63 (n<=39356): PASS

## first-hand (at-commit tree ver-4b3e3e8)
- parents: 1b15add (band71) + 4a3a672 (R63).
- C byte-identical to band71 (cmp); py byte-identical to R63.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band71 C (n<=39036) VERIFY-1b15add GREEN; the
  R63 pins 39037..39356 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
