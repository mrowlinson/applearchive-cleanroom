# VERIFY-ac1ec02 cport band50 T10R47+T10P490..T10P49B (n<=33816): PASS

## first-hand (at-commit tree ver-ac1ec02, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band49.
- parity own run (solo): RGRAMC-PYID 2016/2016
 covered=2016/2016 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band49 (15): T10P490 T10P490C T10P491
 T10P491C T10P49A T10P49AC T10P49B T10P49BC T10R47A T10R47AC
 T10R47AM T10R47AQ T10R47B T10R47BC T10R47BM.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band50 FULL 2016/2016 py-identical, C RGRAM-GREEN)
