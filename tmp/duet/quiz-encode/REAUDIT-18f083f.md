# REAUDIT-18f083f cport band146 T10P115 (n<=56848, 764 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 18f083f
  under WS tmp/encode-viewer/
  18f083f-r21/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7144 lines =
  7142 + 2 header, 3571 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/18f083f-r21/
  build/rgramc-r21 1723944 bytes,
  built first-hand this seat r21).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r21 bin, own-seat
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3571/3571 covered=3571/3571
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r21-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7142 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7142 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7142/7142 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 56757..56848:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 4463b37
  (lane diff = src/c/rgramc.c only,
  +1387/-915; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r21b146.py, textual
  C-vs-py parse): NEW 15/15 EQ GREEN
  (AC 77 rows + BC 67 + QC 63 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2024/0 (1D 166 + 2D
  752 + STR 203 + STRARR 903 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-18f083f +
  VERIFY-18f083f PASS on file,
  merged (bc39521); CLAIM-viewer-
  18f083f-r21 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
