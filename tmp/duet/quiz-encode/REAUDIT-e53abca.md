# REAUDIT-e53abca cport band156 T10P120 (n<=58588, 803 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of e53abca
  under WS tmp/encode-viewer/
  e53abca-r19/tree (seat-private per
  PARENT-038; all data NVME
  PARENT-027). PINS 7390 lines =
  7388 + 2 header, 3694 closed.
- C build 0 warnings (-O2 -Wall
  -Wextra -std=c11, rc=0, own bin
  tmp/encode-viewer/e53abca-r19/
  build/rgramc-r19 1775384 bytes,
  built first-hand this seat r19).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r19 bin, own-seat r19
  corpus seed 8384 hardlinks +
  fresh-oracle new N): RGRAMC-PYID
  3694/3694 covered=3694/3694
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r19-bin>
  tests/test_rgram.sh` own run:
  RGRAM-GREEN (7388 PASS, 0 FAIL,
  rc=0).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7388 PASS, 0 FAIL,
  rc=0).
- C/py PASS-name sets cmp-identical
  7388/7388 (both all-PASS) —
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 58497..58588:
  92 pass / 0 fail (py+C agree
  CLOSED all 92, rc+stdout+stderr
  identical); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  writer-merge parent 827a4ba
  (lane diff = src/c/rgramc.c only,
  +1439/-951; no tmp/ changes).
- tables-EQ own script
  (tables-audit-r19b156.py, textual
  C-vs-py parse): NEW 15/15 EQ GREEN
  (AC 75 rows + BC 72 + QC 68 = py;
  _N derived 3/3; +M38 strarr EQ;
  GATE counted 14 — extra table EQ,
  not mismatch) + FULL audit 2091/0
  (1D 166 + 2D 772 + STR 218 +
  STRARR 935 incl 11 VALS-N).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|
  libcompression|depload|dlopen|
  dylib): 0 hits.
- REAUDIT ordered: GATE-e53abca +
  VERIFY-e53abca PASS on file,
  merged; CLAIM-viewer-e53abca-r19
  oldest live claim (field clear at
  claim + pre-filing re-check, no
  rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
