# REAUDIT-ef51ec3 cport band162 T10P123 (n<=59632, 796 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of ef51ec3
  under WS tmp/encode-viewer/
  ef51ec3-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7538 lines =
  7536 + 2 header, 3768 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/ef51ec3-r19/
  build/rgramc-r19 1809464 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r19
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3768/3768 covered=3768/3768
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7536 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7536 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7536/7536 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 59541..59632:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent ef51ec3^
  (lane diff = src/c/rgramc.c only,
  +1422/-1081; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b162.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  (AC 76 rows + BC 70 + QC 64 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2129/0 (1D 166 + 2D
  784 + STR 225 + STRARR 954 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-ef51ec3 +
  VERIFY-ef51ec3 PASS on file,
  merged; CLAIM-viewer-ef51ec3-r19
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
