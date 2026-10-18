# VERIFY-bac386a cport band58 T10P54+T10R53 (n<=35876): PASS

## first-hand (at-commit tree ver-bac386a, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band57.
- parity own run (solo): RGRAMC-PYID 2126/2126
 covered=2126/2126 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band57 (17): T10P540 T10P541 T10P54A T10P54AC
 T10P54AM T10P54B T10P54BC T10P54BM T10P54S0 T10P54S1 T10R53A
 T10R53AC T10R53AM T10R53AQ T10R53B T10R53BC T10R53BM.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band58 FULL 2126/2126 py-identical, C RGRAM-GREEN)
