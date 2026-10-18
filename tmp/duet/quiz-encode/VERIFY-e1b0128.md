# VERIFY-e1b0128 cport band45 T10R44 (n<=32744, 471 tiers): PASS

## first-hand (at-commit tree ver-e1b0128, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band44.
- parity own run (solo): RGRAMC-PYID 1946/1946
 covered=1946/1946 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10R44 T10R44C T10R44M T10R44QH.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band45 FULL 1946/1946 py-identical, C RGRAM-GREEN)
