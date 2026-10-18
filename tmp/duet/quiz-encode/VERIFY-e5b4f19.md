# VERIFY-e5b4f19 cport band49 T10P480..T10P48B (n<=33468): PASS

## first-hand (at-commit tree ver-e5b4f19, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band48.
- parity own run (solo): RGRAMC-PYID 1996/1996
 covered=1996/1996 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band48 (8): T10P480 T10P480C T10P481 T10P481C
 T10P48A T10P48AC T10P48B T10P48BC (no M/Q — short tier).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band49 FULL 1996/1996 py-identical, C RGRAM-GREEN)
