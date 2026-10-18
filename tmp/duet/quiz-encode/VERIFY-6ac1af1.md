# VERIFY-6ac1af1 cport band47 T10P470..T10P47Q (n<=33184): PASS

## first-hand (at-commit tree ver-6ac1af1, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band46.
- parity own run (solo): RGRAMC-PYID 1976/1976
 covered=1976/1976 => RGRAMC-GREEN. FULL, zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band46 (11): T10P470 T10P470C T10P471
 T10P471C T10P47A T10P47AC T10P47B T10P47BC T10P47M T10P47Q
 T10P47QC.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band47 FULL 1976/1976 py-identical, C RGRAM-GREEN)
