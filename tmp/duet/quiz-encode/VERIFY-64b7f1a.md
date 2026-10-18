# VERIFY-64b7f1a cport band17 T10PS0..T10PSQ (n<=26572, 368 tiers): PASS

## first-hand (at-commit tree ver-64b7f1a, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1602/1602 covered=1602/1602 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 876 static tables (+10 vs band16), growth
  consistent with T10PS0..PSQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band17 FULL 1602/1602 py-identical, C RGRAM-GREEN)
