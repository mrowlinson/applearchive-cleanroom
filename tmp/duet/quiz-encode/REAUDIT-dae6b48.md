# REAUDIT-dae6b48 cport band152 T10P118 (n<=57892, 776 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of dae6b48
  under WS tmp/encode-viewer/
  dae6b48-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7290 lines =
  7288 + 2 header, 3644 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/dae6b48-r19/
  build/rgramc-r19 1758088 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r19
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3644/3644 covered=3644/3644
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7288 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7288 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7288/7288 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 57801..57892:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent d497e00
  (lane diff = src/c/rgramc.c only,
  +1400/-937; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b152.py, textual
  C-vs-py parse): NEW 14/14 EQ GREEN
  (AC 76 rows + BC 72 + QC 64 = py;
  _N derived 3/3; strarr/str rest)
  + FULL audit 2064/0 (1D 166 + 2D
  764 + STR 212 + STRARR 922 incl
  11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-dae6b48 +
  VERIFY-dae6b48 PASS on file,
  merged; CLAIM-viewer-dae6b48-r19
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
