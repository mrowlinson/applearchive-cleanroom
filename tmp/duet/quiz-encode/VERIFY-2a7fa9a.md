# VERIFY-2a7fa9a merge64 P63 (n<=38688): PASS

## first-hand (at-commit tree ver-2a7fa9a)
- parents: a63744d (band69) + 5e0909c (P63).
- C byte-identical to band69 (cmp); py byte-identical to P63.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band69 C (n<=38660) VERIFY-a63744d GREEN; the
  P63 pins 38661..38688 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
