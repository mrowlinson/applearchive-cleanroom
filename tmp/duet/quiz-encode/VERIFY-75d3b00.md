# VERIFY-75d3b00 merge42 band47+R46 (n<=33440): PASS

## first-hand (at-commit tree ver-75d3b00)
- parents: 6ac1af1 (band47) + 804eb41 (R46).
- C byte-identical to band47 (cmp); py byte-identical to R46.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band47 binary: RGRAMC-PYID 1976/1976
 covered=1976/1986 GREEN — the 10 new R46 pins correctly
 UNCOVERED by band47 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
