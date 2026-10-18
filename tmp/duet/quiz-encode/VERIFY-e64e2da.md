# VERIFY-e64e2da cport band6 T10PL0..T10R20 (n<=24392, 327 tiers): PASS

## first-hand (at-commit tree ver-e64e2da, seat-local build)
- C build: rc=0, 0 warnings. single-file delta (rgramc.c).
- parity own run: RGRAMC-PYID 1484/1484 covered=1484/1484 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z24392-closed,
  PASS g-z24392).
- code-read: 791 static tables (+13 vs band5), growth
  consistent with T10PL0..T10R20 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band6 FULL 1484/1484 py-identical, C RGRAM-GREEN)
