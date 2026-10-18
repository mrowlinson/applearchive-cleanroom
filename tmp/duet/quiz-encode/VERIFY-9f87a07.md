# VERIFY-9f87a07 cport band24 T10R31 (n<=28220, 393 tiers): PASS

## first-hand (at-commit tree ver-9f87a07, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1686/1686 covered=1686/1686 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 927 static tables (+2 vs band23: single R31
  tier with q=PWM reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band24 FULL 1686/1686 py-identical, C RGRAM-GREEN)
