# REAUDIT-cf2775e cport band150 T10P117 (n<=57544, 772 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of cf2775e
  under WS tmp/encode-viewer/
  cf2775e-r20/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7240 lines =
  7238 + 2 header, 3619 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/cf2775e-r20/
  build/rgramc-r20 1741208 bytes,
  built first-hand this seat r20).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r20 bin, own-seat
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3619/3619 covered=3619/3619
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r20-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7238 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7238 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7238/7238 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 57453..57544:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 56782d2
  (lane diff = src/c/rgramc.c only,
  +1390/-930; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r20b150.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC 74 rows + BC 67 + QC 66 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2051/0 (1D 166 + 2D
  760 + STR 209 + STRARR 916 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-cf2775e +
  VERIFY-cf2775e PASS on file,
  merged; CLAIM-viewer-cf2775e-r20
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
