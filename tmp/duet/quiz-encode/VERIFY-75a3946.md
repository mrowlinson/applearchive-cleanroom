# VERIFY-75a3946 merge46 band51+P50 (n<=34164): PASS

## first-hand (at-commit tree ver-75a3946)
- parents: 63711c4 (band51) + 94927a9 (P50).
- C byte-identical to band51 (cmp); py byte-identical to P50.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band51 binary: RGRAMC-PYID 2026/2026
 covered=2026/2036 GREEN — the 10 new P50 pins correctly
 UNCOVERED by band51 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
