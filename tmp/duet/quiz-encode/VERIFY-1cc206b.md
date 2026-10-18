# VERIFY-1cc206b cport band22 T10R30 (n<=27872, 387 tiers): PASS

## first-hand (at-commit tree ver-1cc206b, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1666/1666 covered=1666/1666 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 915 static tables (+2 vs band21: single R30
  tier with q=CORE reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band22 FULL 1666/1666 py-identical, C RGRAM-GREEN)
