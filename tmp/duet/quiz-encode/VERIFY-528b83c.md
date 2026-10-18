# VERIFY-528b83c cport band48 T10R46 (n<=33440, 484 tiers): PASS

## first-hand (at-commit tree ver-528b83c, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band47.
- parity own run (solo): RGRAMC-PYID 1986/1986
 covered=1986/1986 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10R46 T10R46C T10R46M.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band48 FULL 1986/1986 py-identical, C RGRAM-GREEN)
