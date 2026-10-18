# REAUDIT-779427a cport band120 T10P102 (n<=52324, 712 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive 779427a under WS
  tmp/encode-viewer/779427a-r23/tree
  (seat-private; all data NVME). PINS
  6502 lines = 6500 + 2 header, 3250 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1570744 bytes, built
  first-hand this seat r23).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r23 bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3250/3250 covered=3250/3250
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r23-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6500 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6500 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6500/6500 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 52233..52324:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent a82a67f
  (lane diff = src/c/rgramc.c only,
  +1287/-835; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r23b120.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  + FULL audit 1860/0 (1D 164 + 2D
  700 + STR 173 + STRARR 823 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-779427a +
  VERIFY-779427a PASS on file,
  merged (d79ae5f); CLAIM-viewer-
  779427a-r23 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
