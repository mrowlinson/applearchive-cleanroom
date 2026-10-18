# VERIFY-8fa0d10 cport band36 T10P400..T10P40Q (n<=30748, 440 tiers): PASS

## first-hand (at-commit tree ver-8fa0d10, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1836/1836 covered=1836/1836 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 1023 static tables (+10 vs band35), growth
  consistent with T10P400..P40Q band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band36 FULL 1836/1836 py-identical, C RGRAM-GREEN)
