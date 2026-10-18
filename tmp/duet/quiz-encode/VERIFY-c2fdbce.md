# VERIFY-c2fdbce cport band27 R33+P35 (n<=29008, 410 tiers): PASS

## first-hand (at-commit tree ver-c2fdbce, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1736/1736 covered=1736/1736 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 961 static tables (+12 vs band26), growth
  consistent with R33+P35 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band27 FULL 1736/1736 py-identical, C RGRAM-GREEN)
