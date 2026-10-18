# REAUDIT-5edb95d cport band160 T10P122 (n<=59284): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 5edb95d
  under WS tmp/encode-viewer/
  5edb95d-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7492 lines =
  7490 + 2 header, 3745 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/5edb95d-r19/
  build/rgramc-r19 1792616 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r19
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3745/3745 covered=3745/3745
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7490 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7490 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7490/7490 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 59193..59284:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 20d2cf4
  (lane diff = src/c/rgramc.c only,
  +1427/-964; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b160.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC 76 rows + BC 72 + QC 65 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2117/0 (1D 166 + 2D
  780 + STR 223 + STRARR 948 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-5edb95d +
  VERIFY-5edb95d PASS on file,
  merged; CLAIM-viewer-5edb95d-r19
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
