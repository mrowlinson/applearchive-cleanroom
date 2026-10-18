# VERIFY-cb10c8b merge55 R55 (n<=36572): PASS

## first-hand (at-commit tree ver-cb10c8b)
- parents: 8255033 (band60) + 3ea1405 (R55).
- C byte-identical to band60 (cmp); py byte-identical to R55.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- C parity: band60 C (n<=36252) VERIFY-8255033 GREEN; the
  R55 pins 36253..36572 are correctly out of its scope, so a
  RGRAM_BIN=C rerun on the merge tree is EXPECTED RED
  (test_rgram.sh has no UNCOVERED semantics — every rc!=0 is
  FAIL). Observed tail: FAIL g36572; direct probe at 36572:
  C rc=2 N out of scope, py CLOSED T10R55B off=255.
  No skew, no defect.

## verdict: PASS (faithful merge, no skew)
