# VERIFY-ba8c96d merge41 band46+P47 (n<=33184): PASS

## first-hand (at-commit tree ver-ba8c96d)
- parents: b9d02c8 (band46) + 0fb3ec8 (P47).
- C byte-identical to band46 (cmp); py byte-identical to P47.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band46 binary: RGRAMC-PYID 1966/1966
 covered=1966/1976 GREEN — the 10 new P47 pins correctly
 UNCOVERED by band46 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
