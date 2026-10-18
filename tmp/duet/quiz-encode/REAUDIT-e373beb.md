# REAUDIT-e373beb cport band140 T10P112 (n<=55804, 752 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive e373beb under WS
  tmp/encode-viewer/e373beb-r22b/tree
  (seat-private; all data NVME). PINS
  6998 lines = 6996 + 2 header, 3498 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1689784 bytes, built
  first-hand this seat r22).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r22b bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3498/3498 covered=3498/3498
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r22b-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6996 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6996 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6996/6996 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 55713..55804:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 5e5947a
  (lane diff = src/c/rgramc.c only,
  +1348/-896; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r22bb140.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC/BC/QC/M/QR/QT/XB + _N
  derived) + FULL audit 1983/0 (1D
  165 + 2D 740 + STR 194 + STRARR
  884 incl 11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-e373beb +
  VERIFY-e373beb + PV-e373beb PASS on
  file, merged (53f78f7); CLAIM-viewer-
  e373beb-r22 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
