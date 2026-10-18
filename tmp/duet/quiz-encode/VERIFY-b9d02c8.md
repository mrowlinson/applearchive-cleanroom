# VERIFY-b9d02c8 cport band46 T10P460..T10P46Q+T10R45 (n<=33092): PASS

## first-hand (at-commit tree ver-b9d02c8, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band45.
- parity own run (solo): RGRAMC-PYID 1966/1966
 covered=1966/1966 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band45 (18): T10P460 T10P460C T10P461
 T10P461C T10P46A T10P46AC T10P46B1 T10P46B1C T10P46B2
 T10P46B2C T10P46M T10P46M32 T10P46Q T10P46QC T10R45 T10R45C
 T10R45M T10R45QH.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band46 FULL 1966/1966 py-identical, C RGRAM-GREEN)
