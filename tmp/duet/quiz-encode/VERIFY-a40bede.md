# VERIFY-a40bede cport band37 T10P410..T10P41Q (n<=31096): PASS

## first-hand (at-commit tree ver-a40bede, seat-local build)
- C build: rc=0, 0 warnings. rgramc.c DIFFERS from band36 (new band).
- parity own run: RGRAMC-PYID 1856/1856 covered=1856/1856 =>
 RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
 oracle): RGRAM-GREEN via C.
- new tables vs band36 (tier-name diff): T10P410 T10P410C T10P411
 T10P411C T10P41A T10P41AC T10P41B T10P41BC T10P41M T10P41Q
 T10P41QC (11 new); `static const` count 1621 vs band36 1604
 (+17, same-command delta).
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band37 FULL 1856/1856 py-identical, C RGRAM-GREEN)
