# VERIFY-84c84e1 cport band9 T10PN0..T10PNQ (n<=24832, 338 tiers): PASS

## first-hand (at-commit tree ver-84c84e1, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1512/1512 covered=1512/1512 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z24832-closed,
  PASS g-z24832).
- code-read: 814 static tables (+10 vs band8), growth
  consistent with T10PN0..PNQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band9 FULL 1512/1512 py-identical, C RGRAM-GREEN)
