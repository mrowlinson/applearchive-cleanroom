# REAUDIT-c14ee5f cport band130 T10P107 (n<=54064, 732 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: git-archive c14ee5f under WS
  tmp/encode-viewer/c14ee5f-r23/tree
  (seat-private; all data NVME). PINS
  6752 lines = 6750 + 2 header, 3375 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  build/rgramc 1622008 bytes, built
  first-hand this seat r23).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r23 bin, same-seat
  corpus seed 7044 hardlinks, fresh
  exec per pin): RGRAMC-PYID
  3375/3375 covered=3375/3375
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r23-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (6750 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (6750 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical
  6750/6750 (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 53973..54064:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent bab78db
  (lane diff = src/c/rgramc.c only,
  +1312/-866; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r23b130.py, textual
  C-vs-py parse): NEW 13/13 EQ GREEN
  + FULL audit 1922/0 (1D 164 + 2D
  720 + STR 184 + STRARR 854 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-c14ee5f +
  VERIFY-c14ee5f PASS on file,
  merged (65d909b); CLAIM-viewer-
  c14ee5f-r23 oldest live claim
  (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
