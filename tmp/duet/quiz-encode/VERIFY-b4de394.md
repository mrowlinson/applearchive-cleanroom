# VERIFY-b4de394 merge67 P65+R64 (n<=39704): PASS

## first-hand (at-commit tree ver-b4de394)
- parents: 581c8f4 (band72) + 012efda (R64).
- C byte-identical to band72 (cmp); py byte-identical to R64.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band72 C (n<=39356) VERIFY-581c8f4 GREEN; the
  P65+R64 pins 39357..39704 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
