# VERIFY-0d8c629 cport band28 T10R34 (n<=29264, 411 tiers): PASS

## first-hand (at-commit tree ver-0d8c629, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1746/1746 covered=1746/1746 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 963 static tables (+2 vs band27: single R34
  tier with q=PZM reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band28 FULL 1746/1746 py-identical, C RGRAM-GREEN)
