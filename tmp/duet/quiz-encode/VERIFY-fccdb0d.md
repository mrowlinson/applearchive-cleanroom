# VERIFY-fccdb0d merge40 band45+P46+R45 (n<=33092): PASS

## first-hand (at-commit tree ver-fccdb0d)
- parents: e1b0128 (band45) + 29272cc (R45).
- C byte-identical to band45 (cmp); py byte-identical to R45.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band45 binary: RGRAMC-PYID 1946/1946
 covered=1946/1966 GREEN — the 20 new P46+R45 pins correctly
 UNCOVERED by band45 C (rc=2 path; GRAMMAR-BREAK signal only
 fires at the 76B→80B transition, not beyond closed 80B).

## verdict: PASS (faithful merge, no skew)
