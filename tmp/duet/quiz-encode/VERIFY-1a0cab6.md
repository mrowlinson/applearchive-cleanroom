# VERIFY-1a0cab6 merge37 band42+R43 (n<=32396): PASS

## first-hand (at-commit tree ver-1a0cab6)
- parents: 4bc35ab (band42) + 9ac84d5 (R43).
- C byte-identical to band42 (cmp); py byte-identical to R43.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band42 binary: RGRAMC-PYID 1916/1916
 covered=1916/1926 GREEN — the 10 new R43 pins correctly
 UNCOVERED by band42 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
