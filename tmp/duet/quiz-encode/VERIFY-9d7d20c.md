# VERIFY-9d7d20c cport band7 T10PM0..T10PMQ (n<=24484, 332 tiers): PASS

## first-hand (at-commit tree ver-9d7d20c, seat-local build)
- C build via new phony alias: rc=0, 0 warnings.
- parity own run: RGRAMC-PYID 1494/1494 covered=1494/1494 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z24484-closed,
  PASS g-z24484).
- code-read: 801 static tables (+10 vs band6), growth
  consistent with T10PM0..PMQ band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band7 FULL 1494/1494 py-identical, C RGRAM-GREEN)
