# VERIFY-a57413b merge70 R66+P68 (n<=40428): PASS

## first-hand (at-commit tree ver-a57413b)
- parents: f563e5f (band75) + cddebe5 (P68).
- C byte-identical to band75 (cmp); py byte-identical to P68.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band75 C (n<=40080) VERIFY-f563e5f GREEN; the
  R66+P68 pins 40081..40428 are correctly out of its scope
  (RGRAM_BIN=C rerun on merge tree EXPECTED RED per
  test_rgram.sh no-UNCOVERED semantics, as VERIFY-cb10c8b).

## verdict: PASS (faithful merge, no skew)
