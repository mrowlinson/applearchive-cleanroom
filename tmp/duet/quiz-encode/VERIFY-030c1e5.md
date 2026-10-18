# VERIFY-030c1e5 merge47 band52+R49+P51 (n<=34512): PASS

## first-hand (at-commit tree ver-030c1e5)
- parents: d840c7b (band52) + cc646bf (P51).
- C byte-identical to band52 (cmp); py byte-identical to P51.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band52 binary: RGRAMC-PYID 2036/2036
 covered=2036/2056 GREEN — the 20 new R49+P51 pins correctly
 UNCOVERED by band52 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
