# VERIFY-8bd65c3 cport band35 T10R38 (n<=30656, 435 tiers): PASS

## first-hand (at-commit tree ver-8bd65c3, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1826/1826 covered=1826/1826 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 1013 static tables (+2 vs band34: single R38
  tier with q=XOR reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band35 FULL 1826/1826 py-identical, C RGRAM-GREEN)
