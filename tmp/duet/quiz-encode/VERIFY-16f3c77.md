# VERIFY-16f3c77 cport band56 T10R51+T10P53 (n<=35208): PASS

## first-hand (at-commit tree ver-16f3c77, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band55.
- parity own run (solo): RGRAMC-PYID 2096/2096
 covered=2096/2096 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band55 (18): T10P530 T10P531 T10P53A T10P53AC
 T10P53AM T10P53B T10P53BC T10P53BM T10P53S0 T10P53S1 T10R51A
 T10R51AC T10R51AM T10R51AQ T10R51B T10R51BC T10R51BM T10R51QH.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band56 FULL 2096/2096 py-identical, C RGRAM-GREEN)
