# VERIFY-77f7545 cport band18 R27+P29 (n<=26920, 374 tiers): PASS

## first-hand (at-commit tree ver-77f7545, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1620/1620 covered=1620/1620 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C.
- code-read: 888 static tables (+12 vs band17), growth
  consistent with R27+P29 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band18 FULL 1620/1620 py-identical, C RGRAM-GREEN)
