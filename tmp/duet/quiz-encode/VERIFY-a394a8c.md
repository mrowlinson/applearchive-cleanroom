# VERIFY-a394a8c merge43 band48+P48 (n<=33468): PASS

## first-hand (at-commit tree ver-a394a8c)
- parents: 528b83c (band48) + 2710640 (P48).
- C byte-identical to band48 (cmp); py byte-identical to P48.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band48 binary: RGRAMC-PYID 1986/1986
 covered=1986/1996 GREEN — the 10 new P48 pins correctly
 UNCOVERED by band48 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
