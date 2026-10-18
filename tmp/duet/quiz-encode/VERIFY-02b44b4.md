# VERIFY-02b44b4 cport band13 T10R24 (n<=25784, 351 tiers): PASS

## first-hand (at-commit tree ver-02b44b4, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1556/1556 covered=1556/1556 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 842 static tables (+3 vs band12: single R24
  tier with q=PPM reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band13 FULL 1556/1556 py-identical, C RGRAM-GREEN)
