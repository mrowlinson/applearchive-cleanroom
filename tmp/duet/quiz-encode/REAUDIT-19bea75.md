# REAUDIT-19bea75 cport band126 T10P105 (n<=53368, 724 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive 19bea75 under WS
  tmp/encode-viewer/19bea75-r23/tree
  (seat-private; all data NVME). PINS
  6652 lines = 6650 + 2 header, 3325 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1604808 bytes, built
  first-hand this seat r23).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r23 bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3325/3325 covered=3325/3325
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r23-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6650 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6650 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6650/6650 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 53277..53368:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 814a732
  (lane diff = src/c/rgramc.c only,
  +1297/-853; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r23b126.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  + FULL audit 1897/0 (1D 164 + 2D
  712 + STR 179 + STRARR 842 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-19bea75 +
  VERIFY-19bea75 PASS on file,
  merged (a166753); CLAIM-viewer-
  19bea75-r23 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
