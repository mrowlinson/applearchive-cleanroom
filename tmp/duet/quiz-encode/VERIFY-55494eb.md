# VERIFY-55494eb cport band15 R25+P27 (n<=26224, 362 tiers): PASS

## first-hand (at-commit tree ver-55494eb, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1584/1584 covered=1584/1584 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 864 static tables (+12 vs band14), growth
  consistent with R25+P27 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band15 FULL 1584/1584 py-identical, C RGRAM-GREEN)
