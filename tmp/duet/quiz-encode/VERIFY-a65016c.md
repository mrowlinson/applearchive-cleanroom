# VERIFY-a65016c cport band39 T10P420..T10P42Q (n<=31444): PASS

## first-hand (at-commit tree ver-a65016c, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band38.
- parity own run (solo): RGRAMC-PYID 1876/1876
 covered=1876/1876 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables: T10P420 T10P420C T10P421 T10P421C T10P42A
 T10P42AC T10P42B T10P42BC T10P42M T10P42MB T10P42Q T10P42QC.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.
- NOTE: first parity run RED only via own-harness-race (two
 parity runs shared one corpus workdir); solo rerun GREEN.

## verdict: PASS (band39 FULL 1876/1876 py-identical, C RGRAM-GREEN)
