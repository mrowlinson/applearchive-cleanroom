# VERIFY-8b8a699 merge34 band39+R41 (n<=31700): PASS

## first-hand (at-commit tree ver-8b8a699)
- parents: a65016c (band39) + 0c7b7fe (R41).
- C byte-identical to band39 (cmp); py byte-identical to R41.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band39 binary: RGRAMC-PYID 1876/1876
 covered=1876/1886 GREEN — the 10 new R41 pins correctly
 UNCOVERED by band39 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
