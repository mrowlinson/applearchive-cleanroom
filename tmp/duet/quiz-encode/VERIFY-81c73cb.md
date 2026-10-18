# VERIFY-81c73cb cport band29 T10P360..T10P36Q (n<=29356, 416 tiers): PASS

## first-hand (at-commit tree ver-81c73cb, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1756/1756 covered=1756/1756 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 973 static tables (+10 vs band28), growth
  consistent with T10P360..P36Q band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band29 FULL 1756/1756 py-identical, C RGRAM-GREEN)
