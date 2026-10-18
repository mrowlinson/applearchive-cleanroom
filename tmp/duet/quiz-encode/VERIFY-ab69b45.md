# VERIFY-ab69b45 cport band38 T10R40 (n<=31352, 447 tiers): PASS

## first-hand (at-commit tree ver-ab69b45, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band37.
- parity own run: RGRAMC-PYID 1866/1866 covered=1866/1866 =>
 RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10R40 T10R40C T10R40M present.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band38 FULL 1866/1866 py-identical, C RGRAM-GREEN)
