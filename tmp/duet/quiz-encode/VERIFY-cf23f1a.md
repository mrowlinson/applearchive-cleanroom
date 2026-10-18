# VERIFY-cf23f1a merge48 band53+R50 (n<=34832): PASS

## first-hand (at-commit tree ver-cf23f1a)
- parents: f15455c (band53) + b8230b7 (R50).
- C byte-identical to band53 (cmp); py byte-identical to R50.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band53 binary: RGRAMC-PYID 2056/2056
 covered=2056/2066 GREEN — the 10 new R50 pins correctly
 UNCOVERED by band53 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
