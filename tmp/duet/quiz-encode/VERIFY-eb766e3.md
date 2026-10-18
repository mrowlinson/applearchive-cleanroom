# VERIFY-eb766e3 cport band4 FULL T9..T10R16 (n<=23000, 303 tiers): PASS

## first-hand (at-commit tree ver-eb766e3, seat-local build)
- C build: rc=0, 0 warnings (35K-line rgramc.c).
- parity own run: RGRAMC-PYID 1411/1411 covered=1411/1411 =>
  RGRAMC-GREEN. FULL coverage: zero uncovered N.
- `RGRAM_BIN=seat-binary tests/test_rgram.sh` (own run, fresh
  oracle): RGRAM-GREEN via C (tail PASS g-z23000-closed,
  PASS g-z23000). python side byte-identical to band1 (3 files
  cmp SAME): python RGRAM-GREEN also carries.
- code-read: 741 static tables + 13 function-local inline
  const pairs (_cN, per-tier balanced-parse consts); full name
  audit 747 C tables: 734 named-in-py + 13 locals explained.
  value spots exact: _T2SCRAM head + T4B3 consts
  (0x0d=13, 0x6c=108, 0x3c=60, 0xf0=240, 0xe1=225...).
  faithful mechanical port, no hand-tuned constants found.
- wall-grep: 0 hits. hygiene: same 13 pre-existing .aar, 0 new.

## verdict: PASS (band4 FULL 1411/1411 py-identical, C RGRAM-GREEN)
