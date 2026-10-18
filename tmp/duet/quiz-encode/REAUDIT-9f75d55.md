# REAUDIT-9f75d55 cport band144 T10P114 (n<=56500, 760 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 9f75d55
  under WS tmp/encode-viewer/
  9f75d55-r21/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7094 lines =
  7092 + 2 header, 3546 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/9f75d55-r21/
  build/rgramc-r21 1707048 bytes,
  built first-hand this seat r21).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r21 bin, own-seat
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3546/3546 covered=3546/3546
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r21-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7092 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7092 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7092/7092 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 56409..56500:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 6e9422a
  (lane diff = src/c/rgramc.c only,
  +1355/-911; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r21b144.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  (AC + BC + QC = py; _N derived
  3/3; strarr/str rest) + FULL
  audit 2010/0 (1D 166 + 2D 748 +
  STR 199 + STRARR 897 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-9f75d55 +
  VERIFY-9f75d55 PASS on file,
  merged (29214a1); CLAIM-viewer-
  9f75d55-r21 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
