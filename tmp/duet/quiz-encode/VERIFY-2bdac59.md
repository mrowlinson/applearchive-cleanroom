# VERIFY-2bdac59 merge75 R70 (n<=41792): PASS

## first-hand (at-commit tree ver-2bdac59)
- parents: 9c4264a (band80) + e34f88e (R70).
- C byte-identical to band80 (cmp); py byte-identical to R70.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band80 C (n<=41472) VERIFY-9c4264a GREEN; the
  R70 pins 41473..41792 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
