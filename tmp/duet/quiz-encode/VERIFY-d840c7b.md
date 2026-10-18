# VERIFY-d840c7b cport band52 T10P500..T10P50B (n<=34164): PASS

## first-hand (at-commit tree ver-d840c7b, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band51.
- parity own run (solo): RGRAMC-PYID 2036/2036
 covered=2036/2036 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band51 (8): T10P500 T10P500C T10P501 T10P501C
 T10P50A T10P50AC T10P50B T10P50BC (no M/Q — short tier).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band52 FULL 2036/2036 py-identical, C RGRAM-GREEN)
