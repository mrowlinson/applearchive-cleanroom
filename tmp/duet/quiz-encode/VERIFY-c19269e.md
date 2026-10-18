# VERIFY-c19269e merge65 R62+P64 (n<=39036): PASS

## first-hand (at-commit tree ver-c19269e)
- parents: 80d12c7 (band70) + d952c6f (P64).
- C byte-identical to band70 (cmp); py byte-identical to P64.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band70 C (n<=38688) VERIFY-80d12c7 GREEN; the
  R62+P64 pins 38689..39036 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
