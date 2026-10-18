# VERIFY-54efe06 merge73 P70 (n<=41124): PASS

## first-hand (at-commit tree ver-54efe06)
- parents: 5ab465c (band78) + 5776851 (P70).
- C byte-identical to band78 (cmp); py byte-identical to P70.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band78 C (n<=41096) VERIFY-5ab465c GREEN; the
  P70 pins 41097..41124 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
