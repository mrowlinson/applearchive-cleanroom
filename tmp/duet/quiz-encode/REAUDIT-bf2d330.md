# REAUDIT-bf2d330 cport band142 T10P113 (n<=56152, 756 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive bf2d330 under WS
  tmp/encode-viewer/bf2d330-r22b/tree
  (seat-private; all data NVME). PINS
  7046 lines = 7044 + 2 header, 3522 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1706696 bytes, built
  first-hand this seat r22).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r22b bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3522/3522 covered=3522/3522
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r22b-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7044 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7044 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  7044/7044 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 56061..56152:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 188be03
  (lane diff = src/c/rgramc.c only,
  +1361/-902; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r22bb142.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC/BC/QC/M/QR/QT/S0-S2 + _N
  derived) + FULL audit 1997/0 (1D
  165 + 2D 744 + STR 197 + STRARR
  891 incl 11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-bf2d330 +
  VERIFY-bf2d330 PASS on file,
  merged (8fa1e54); CLAIM-viewer-
  bf2d330-r22 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
