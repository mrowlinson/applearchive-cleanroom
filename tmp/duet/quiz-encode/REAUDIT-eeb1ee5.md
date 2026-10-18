# REAUDIT-eeb1ee5 cport band110 T10P96+T10R94 (n<=50492, 690 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive eeb1ee5 under WS
  NVME tmp/encode-viewer/eeb1ee5-r24/tree
  (seat-private; all data NVME). PINS
  6212 lines = 6210 + 2 header, 3105 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1519192 bytes, built
  first-hand this seat r24).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r24 bin, same-seat
  corpus seed 3522 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3105/3105 covered=3105/3105
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r24-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6210 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6210 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6210/6210 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 50145..50492:
  348 pass / 0 fail (py+C agree
  CLOSED all 348, rc+stdout+stderr
  identical); pins 52/52 (26 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 5e72665
  (lane diff = src/c/rgramc.c only,
  +1378/-799; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r24b110.py, textual
  C-vs-py parse): NEW 16/16 EQ GREEN
  + FULL audit 1787/0 (1D 164 + 2D
  677 + STR 161 + STRARR 785 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib + extended): 0 hits.
- REAUDIT ordered: GATE-eeb1ee5 +
  VERIFY-eeb1ee5 PASS on file,
  merged (0fa8d24); CLAIM-viewer-
  eeb1ee5-r24 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
