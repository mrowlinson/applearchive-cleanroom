# VERIFY-4c9ff15 cport band196 T10P140 (n<=65548, 864 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 4c9ff15
  under WS tmp/encode-viewer/
  4c9ff15-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 8386 lines =
  8384 + 2 header, 4192 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/4c9ff15-r19/
  build/rgramc-r19 1997368 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r18
  corpus seed 8304 hardlinks + fresh-
  oracle new N): RGRAMC-PYID
  4192/4192 covered=4192/4192
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (8384 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (8384 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  8384/8384 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 65457..65548:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 30/30 (15 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 55a1a81 (lane
  diff = src/c/rgramc.c only,
  +1559/-1081; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b196.py, textual
  C-vs-py parse): NEW 15/15 EQ GREEN
  (AC 76 rows + BC 71 + QC 62 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2354/0 (1D 167 + 2D
  852 + STR 268 + STRARR 1067 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- GATE-first ordered: GATE-4c9ff15
  PASS-functional on file (sweep2-
  r19, no FLAG); CLAIM-viewer-
  4c9ff15-r19 oldest live verifier
  claim (viewer3-r10 claim stale:
  seat dead 100min at claim, PYID
  incomplete, no handoff; field
  clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
