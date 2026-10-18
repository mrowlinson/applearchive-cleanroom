# REAUDIT-7081fd5 cport band124 T10P104 (n<=53020, 720 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive 7081fd5 under WS
  tmp/encode-viewer/7081fd5-r23/tree
  (seat-private; all data NVME). PINS
  6602 lines = 6600 + 2 header, 3300 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1587960 bytes, built
  first-hand this seat r23).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r23 bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3300/3300 covered=3300/3300
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r23-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6600 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6600 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6600/6600 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 52929..53020:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent dc5d75b
  (lane diff = src/c/rgramc.c only,
  +1287/-847; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r23b124.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  + FULL audit 1885/0 (1D 164 + 2D
  708 + STR 177 + STRARR 836 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-7081fd5 +
  VERIFY-7081fd5 PASS on file,
  merged (0dd2451); CLAIM-viewer-
  7081fd5-r23 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
