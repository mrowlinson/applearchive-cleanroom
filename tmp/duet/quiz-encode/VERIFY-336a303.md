# VERIFY-336a303 cport band23 T10PW0..T10PWQ (n<=27964, 392 tiers): PASS

## first-hand (at-commit tree ver-336a303, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1676/1676 covered=1676/1676 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 925 static tables (+10 vs band22), growth
  consistent with T10PW0..PWQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band23 FULL 1676/1676 py-identical, C RGRAM-GREEN)
