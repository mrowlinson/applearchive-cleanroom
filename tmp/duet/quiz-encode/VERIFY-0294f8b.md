# VERIFY-0294f8b cport band41 T10P430..T10P43Q+T10R42 (n<=32048): PASS

## first-hand (at-commit tree ver-0294f8b, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band40.
- parity own run (solo): RGRAMC-PYID 1906/1906
 covered=1906/1906 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band40: T10P430 T10P430C T10P431 T10P431C
 T10P43A T10P43AC T10P43B T10P43BC T10P43M T10P43Q T10P43QC
 T10R42 T10R42C T10R42M T10R42QH (15 new).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band41 FULL 1906/1906 py-identical, C RGRAM-GREEN)
