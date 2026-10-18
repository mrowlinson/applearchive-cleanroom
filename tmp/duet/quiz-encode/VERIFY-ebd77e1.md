# VERIFY-ebd77e1 merge32 band37+R40 (n<=31352): PASS

## first-hand (at-commit tree ver-ebd77e1)
- parents: a40bede (band37) + 497b4f4 (R40).
- C byte-identical to band37 (cmp); py byte-identical to R40;
 PINS byte-identical to R40.
- harness diff w2-vs-merge test_rgram.sh: RGRAM_BIN override
 lines only (2 lines).
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band37 binary: RGRAMC-PYID 1856/1856
 covered=1856/1866 GREEN — the 10 new R40 pins correctly
 UNCOVERED by band37 C (out of its scope), zero mismatches.

## verdict: PASS (faithful merge, no skew)
