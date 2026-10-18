# VERIFY-8ca0c31 merge38 band43+P45 (n<=32488): PASS

## first-hand (at-commit tree ver-8ca0c31)
- parents: 7c75537 (band43) + ef80529 (P45).
- C byte-identical to band43 (cmp); py byte-identical to P45.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band43 binary: RGRAMC-PYID 1926/1926
 covered=1926/1936 GREEN — the 10 new P45 pins correctly
 UNCOVERED by band43 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
