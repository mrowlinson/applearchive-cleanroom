# VERIFY-4bc35ab cport band42 T10P440..T10P44Q (n<=32140): PASS

## first-hand (at-commit tree ver-4bc35ab, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band41.
- parity own run (solo): RGRAMC-PYID 1916/1916
 covered=1916/1916 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band41: T10P440 T10P440C T10P441 T10P441C
 T10P44A T10P44AC T10P44B T10P44BC T10P44M T10P44Q T10P44QC
 (11 new).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band42 FULL 1916/1916 py-identical, C RGRAM-GREEN)
