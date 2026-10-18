# REAUDIT-77afc34 cport band154 T10P119 (n<=58240, 789 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 77afc34
  under WS tmp/encode-viewer/
  77afc34-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7340 lines =
  7338 + 2 header, 3669 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/77afc34-r19/
  build/rgramc-r19 1758440 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r19
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3669/3669 covered=3669/3669
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7338 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7338 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7338/7338 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 58149..58240:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 3ba738b
  (lane diff = src/c/rgramc.c only,
  +1407/-944; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b154.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC 77 rows + BC 70 + QC 63 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2077/0 (1D 166 + 2D
  768 + STR 215 + STRARR 928 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-77afc34 +
  VERIFY-77afc34 PASS on file,
  merged; CLAIM-viewer-77afc34-r19
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
