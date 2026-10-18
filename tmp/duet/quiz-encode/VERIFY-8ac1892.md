# VERIFY-8ac1892 merge36 band41+P44 (n<=32140): PASS

## first-hand (at-commit tree ver-8ac1892)
- parents: 0294f8b (band41) + ea1b509 (P44).
- C byte-identical to band41 (cmp); py byte-identical to P44.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band41 binary: RGRAMC-PYID 1906/1906
 covered=1906/1916 GREEN — the 10 new P44 pins correctly
 UNCOVERED by band41 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
