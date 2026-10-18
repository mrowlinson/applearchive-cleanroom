# VERIFY-3b46081 merge45 band50+R48 (n<=34136): PASS

## first-hand (at-commit tree ver-3b46081)
- parents: ac1ec02 (band50) + 838cde4 (R48).
- C byte-identical to band50 (cmp); py byte-identical to R48.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band50 binary: RGRAMC-PYID 2016/2016
 covered=2016/2026 GREEN — the 10 new R48 pins correctly
 UNCOVERED by band50 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
