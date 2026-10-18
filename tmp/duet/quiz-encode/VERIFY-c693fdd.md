# VERIFY-c693fdd cport band44 T10P450..T10P45Q (n<=32488): PASS

## first-hand (at-commit tree ver-c693fdd, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band43.
- parity own run (solo): RGRAMC-PYID 1936/1936
 covered=1936/1936 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band43: T10P450 T10P450C T10P451 T10P451C
 T10P45A T10P45AC T10P45B T10P45BC T10P45M T10P45M14 T10P45M25
 T10P45Q T10P45QC (13 new).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band44 FULL 1936/1936 py-identical, C RGRAM-GREEN)
