# VERIFY-91f70b6 merge76 P72+R71 (n<=42140): PASS

## first-hand (at-commit tree ver-91f70b6)
- parents: 3184de5 (band81) + 60aa85b (R71).
- C byte-identical to band81 (cmp); py byte-identical to R71.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band81 C (n<=41792) VERIFY-3184de5 GREEN; the
  P72+R71 pins 41793..42140 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
