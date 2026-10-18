# VERIFY-bb05dd4 merge35 band40+P43+R42 (n<=32048): PASS

## first-hand (at-commit tree ver-bb05dd4)
- parents: 1b84bca (band40) + cf113e3 (R42).
- C byte-identical to band40 (cmp); py byte-identical to R42.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band40 binary: RGRAMC-PYID 1886/1886
 covered=1886/1906 GREEN — the 20 new P43+R42 pins correctly
 UNCOVERED by band40 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
