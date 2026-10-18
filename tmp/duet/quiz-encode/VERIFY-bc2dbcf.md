# VERIFY-bc2dbcf merge44 band49+R47+P49 (n<=33816): PASS

## first-hand (at-commit tree ver-bc2dbcf)
- parents: e5b4f19 (band49) + 9d89fac (P49).
- C byte-identical to band49 (cmp); py byte-identical to P49.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band49 binary: RGRAMC-PYID 1996/1996
 covered=1996/2016 GREEN — the 20 new R47+P49 pins correctly
 UNCOVERED by band49 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
