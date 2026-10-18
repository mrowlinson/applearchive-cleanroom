# VERIFY-f15455c cport band53 T10R49+T10P510..T10P51B (n<=34512): PASS

## first-hand (at-commit tree ver-f15455c, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band52.
- parity own run (solo): RGRAMC-PYID 2056/2056
 covered=2056/2056 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band52 (16): T10P510 T10P510C T10P511
 T10P511C T10P51A T10P51AC T10P51B T10P51BC T10R49A T10R49AC
 T10R49AM T10R49AQ T10R49B T10R49BC T10R49BM T10R49QH.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band53 FULL 2056/2056 py-identical, C RGRAM-GREEN)
