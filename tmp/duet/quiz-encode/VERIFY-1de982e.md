# VERIFY-1de982e cport band30 T10R35 (n<=29612, 417 tiers): PASS

## first-hand (at-commit tree ver-1de982e, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1766/1766 covered=1766/1766 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 975 static tables (+2 vs band29: single R35
  tier with q=P36M reuse => tiny delta, consistent), scope
  gate above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band30 FULL 1766/1766 py-identical, C RGRAM-GREEN)
