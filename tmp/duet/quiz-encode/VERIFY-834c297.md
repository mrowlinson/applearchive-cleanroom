# VERIFY-834c297 cport band12 R23+P25 (n<=25528, 350 tiers): PASS

## first-hand (at-commit tree ver-834c297, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1548/1548 covered=1548/1548 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 839 static tables (+13 vs band11), growth
  consistent with R23+P25 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band12 FULL 1548/1548 py-identical, C RGRAM-GREEN)
