# VERIFY-d3247df cport band25 P33+R32 (n<=28568, 399 tiers): PASS

## first-hand (at-commit tree ver-d3247df, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1706/1706 covered=1706/1706 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 939 static tables (+12 vs band24), growth
  consistent with P33+R32 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band25 FULL 1706/1706 py-identical, C RGRAM-GREEN)
