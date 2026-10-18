# VERIFY-4ad7a4d cport band16 T10R26 (n<=26480, 363 tiers): PASS

## first-hand (at-commit tree ver-4ad7a4d, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1592/1592 covered=1592/1592 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 866 static tables (+2 vs band15: single R26
  tier with q=PRM reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band16 FULL 1592/1592 py-identical, C RGRAM-GREEN)
