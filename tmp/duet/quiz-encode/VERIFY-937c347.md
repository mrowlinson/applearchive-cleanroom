# VERIFY-937c347 cport band5 T10PI0..T10R19 (n<=24044, 321 tiers): PASS

## first-hand (at-commit tree ver-937c347, seat-local build)
- C build: rc=0, 0 warnings. single-file delta (rgramc.c).
- parity own run: RGRAMC-PYID 1466/1466 covered=1466/1466 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z24044-closed,
  PASS g-z24044).
- code-read: 778 static tables (+37 vs band4), growth
  consistent with T10PI0..T10R19 band range; scope gate above
  band intact.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band5 FULL 1466/1466 py-identical, C RGRAM-GREEN)
