# VERIFY-6b87eaf cport band21 T10PV0..T10PVQ (n<=27616, 386 tiers): PASS

## first-hand (at-commit tree ver-6b87eaf, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1656/1656 covered=1656/1656 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 913 static tables (+10 vs band20), growth
  consistent with T10PV0..PVQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band21 FULL 1656/1656 py-identical, C RGRAM-GREEN)
