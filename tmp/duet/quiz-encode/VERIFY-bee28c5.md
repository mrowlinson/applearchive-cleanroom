# VERIFY-bee28c5 merge68 P66 (n<=39732): PASS

## first-hand (at-commit tree ver-bee28c5)
- parents: d0484b7 (band73) + 3682200 (P66).
- C byte-identical to band73 (cmp); py byte-identical to P66.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band73 C (n<=39704) VERIFY-d0484b7 GREEN; the
  P66 pins 39705..39732 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
