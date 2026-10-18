# VERIFY-23f6d99 merge33 band38+P42 (n<=31444): PASS

## first-hand (at-commit tree ver-23f6d99)
- parents: ab69b45 (band38) + a0e16b3 (P42).
- C byte-identical to band38 (cmp); py byte-identical to P42;
 PINS byte-identical to P42.
- `tests/test_rgram.sh` own run fresh oracle: RGRAM-GREEN.
- parity via reused band38 binary: RGRAMC-PYID 1866/1866
 covered=1866/1876 GREEN — the 10 new P42 pins correctly
 UNCOVERED by band38 C (out of its scope), zero mismatches.
- NOTE own-harness-race: first reuse run concurrent with a
 second parity run on the shared corpus workdir showed bogus
 RED (cross-talk via shared py.out/c.out); solo rerun GREEN.
 Lesson: never run two parity harnesses on one workdir.

## verdict: PASS (faithful merge, no skew)
