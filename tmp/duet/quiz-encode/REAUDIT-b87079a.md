# REAUDIT-b87079a cport band138 T10P111 (n<=55456, 748 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive b87079a under WS
  tmp/encode-viewer/b87079a-r22b/tree
  (seat-private; all data NVME). PINS
  6950 lines = 6948 + 2 header, 3474 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1672920 bytes, built
  first-hand this seat r22).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r22b bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3474/3474 covered=3474/3474
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r22b-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6948 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6948 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6948/6948 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 55365..55456:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent e5b435f
  (lane diff = src/c/rgramc.c only,
  +1336/-890; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r22bb138.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  + FULL audit 1970/0 (1D 164 + 2D
  736 + STR 192 + STRARR 878 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-b87079a +
  VERIFY-b87079a + PV-b87079a PASS on
  file, merged (a340479); CLAIM-viewer-
  b87079a-r22 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
