# VERIFY-40c2817 merge72 P69+R68 (n<=41096): PASS

## first-hand (at-commit tree ver-40c2817)
- parents: cc81d7f (band77) + 911b25f (R68).
- C byte-identical to band77 (cmp); py byte-identical to R68.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band77 C (n<=40748) VERIFY-cc81d7f GREEN; the
  P69+R68 pins 40749..41096 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
