# VERIFY-a99d06a cport band10 T10R22 (n<=25088, 339 tiers): PASS

## first-hand (at-commit tree ver-a99d06a, seat-local build)
- C build via phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1520/1520 covered=1520/1520 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail g-z25088 zone).
- code-read: 816 static tables (+2 vs band9: single R22 tier
  with q=PNM reuse => tiny delta, consistent), scope gate
  above band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band10 FULL 1520/1520 py-identical, C RGRAM-GREEN)
