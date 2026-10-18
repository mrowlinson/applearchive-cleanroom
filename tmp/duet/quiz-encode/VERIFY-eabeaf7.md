# VERIFY-eabeaf7 merge39 band44+R44 (n<=32744): PASS (explained reuse-RED)

## first-hand (at-commit tree ver-eabeaf7)
- parents: c693fdd (band44) + 074bf0a (R44).
- C byte-identical to band44 (cmp); py byte-identical to R44.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band44 binary: RGRAMC-PYID 1936/1946
 covered=1946/1946 RGRAMC-RED — 10 mismatches, all in R44
 range (32489..32744).
- root cause (probed first-hand): band44 C answers those N
 with `GRAMMAR-BREAK paylen 80` rc=1, NOT `N out of scope`
 rc=2 — so the harness counts them covered-but-mismatched
 vs R44 py (which CLOSES them).
- NOT a code defect: band44 C == P45-era py on all 10 pins
 (10/10 same output + same rc=1, own loop). The C binary
 faithfully reproduces its own py's out-of-scope signal;
 the signal itself changed at the 80B transition (rc=2 →
 GRAMMAR-BREAK rc=1). Cross-version RED is expected here.
- harness gap (for cport lane): UNCOVERED definition accepts
 only rc=2; GRAMMAR-BREAK rc=1 from an older C should also
 count as uncovered when py closes the N.

## verdict: PASS (faithful merge; reuse-RED explained, C faithful)
