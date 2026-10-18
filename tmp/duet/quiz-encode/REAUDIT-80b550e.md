# REAUDIT-80b550e cport band136 T10P110 (n<=55108, 744 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive 80b550e under WS
  tmp/encode-viewer/80b550e-r22b/tree
  (seat-private; all data NVME). PINS
  6900 lines = 6898 + 2 header, 3449 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1672584 bytes, built
  first-hand this seat r22).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r22b bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3449/3449 covered=3449/3449
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r22b-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6898 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6898 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6898/6898 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 55017..55108:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent c72589f
  (lane diff = src/c/rgramc.c only,
  +1330/-884; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r22bb136.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  + FULL audit 1958/0 (1D 164 + 2D
  732 + STR 190 + STRARR 872 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-80b550e +
  VERIFY-80b550e PASS on file,
  merged (cf65443); CLAIM-viewer-
  80b550e-r22 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
