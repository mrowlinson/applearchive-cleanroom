# VERIFY-2f50789 merge51 band56+R52 (n<=35528): PASS

## first-hand (at-commit tree ver-2f50789)
- parents: 16f3c77 (band56) + b5a223f (R52).
- C byte-identical to band56 (cmp); py byte-identical to R52.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band56 binary: RGRAMC-PYID 2096/2096
 covered=2096/2106 GREEN — the 10 new R52 pins correctly
 UNCOVERED by band56 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
