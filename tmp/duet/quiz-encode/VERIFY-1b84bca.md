# VERIFY-1b84bca cport band40 T10R41 (n<=31700, 453 tiers): PASS

## first-hand (at-commit tree ver-1b84bca, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band39.
- parity own run (solo): RGRAMC-PYID 1886/1886
 covered=1886/1886 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10R41 T10R41C T10R41M T10R41QH.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band40 FULL 1886/1886 py-identical, C RGRAM-GREEN)
