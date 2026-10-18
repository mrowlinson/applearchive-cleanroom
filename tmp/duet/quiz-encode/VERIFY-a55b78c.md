# VERIFY-a55b78c cport band19 T10R28 (n<=27176, 375 tiers): PASS

## first-hand (at-commit tree ver-a55b78c, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1628/1628 covered=1628/1628 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 890 static tables (+2 vs band18: single R28
  tier with q=PTM reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band19 FULL 1628/1628 py-identical, C RGRAM-GREEN)
