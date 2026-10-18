# VERIFY-7c75537 cport band43 T10R43 (n<=32396, 465 tiers): PASS

## first-hand (at-commit tree ver-7c75537, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band42.
- parity own run (solo): RGRAMC-PYID 1926/1926
 covered=1926/1926 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10R43 T10R43C T10R43M.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band43 FULL 1926/1926 py-identical, C RGRAM-GREEN)
