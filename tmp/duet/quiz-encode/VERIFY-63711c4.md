# VERIFY-63711c4 cport band51 T10R48 (n<=34136, 496 tiers): PASS

## first-hand (at-commit tree ver-63711c4, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band50.
- parity own run (solo): RGRAMC-PYID 2026/2026
 covered=2026/2026 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band50 (7): T10R48A T10R48AC T10R48AM
 T10R48AQ T10R48B T10R48BC T10R48BM.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band51 FULL 2026/2026 py-identical, C RGRAM-GREEN)
