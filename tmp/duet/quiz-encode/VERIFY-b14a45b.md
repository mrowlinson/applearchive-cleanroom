# VERIFY-b14a45b cport band32 R36+P38 (n<=30052, 428 tiers): PASS

## first-hand (at-commit tree ver-b14a45b, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1796/1796 covered=1796/1796 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 998 static tables (+13 vs band31), growth
  consistent with R36+P38 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band32 FULL 1796/1796 py-identical, C RGRAM-GREEN)
