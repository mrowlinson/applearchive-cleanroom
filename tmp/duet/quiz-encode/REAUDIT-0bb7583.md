# REAUDIT-0bb7583 cport band148 T10P116 (n<=57196, 768 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 0bb7583
  under WS tmp/encode-viewer/
  0bb7583-r20/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7192 lines =
  7190 + 2 header, 3595 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/0bb7583-r20/
  build/rgramc-r20 1724344 bytes,
  built first-hand this seat r20).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r20 bin, own-seat
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3595/3595 covered=3595/3595
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r20-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7190 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7190 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7190/7190 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 57105..57196:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent fd02d44
  (lane diff = src/c/rgramc.c only,
  +1383/-923; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r20b148.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC/BC/QC = py; _N derived 3/3;
  strarr/str rest) + FULL audit
  2038/0 (1D 166 + 2D 756 + STR 206
  + STRARR 910 incl 11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-0bb7583 +
  VERIFY-0bb7583 PASS on file,
  merged; CLAIM-viewer-0bb7583-r20
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
