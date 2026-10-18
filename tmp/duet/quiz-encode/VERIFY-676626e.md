# VERIFY-676626e cport band194 T10P139 (n<=65200, 860 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 676626e under WS
  tmp/encode-viewer2/676626e/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 676626e confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/676626e/build-r10/
  rgramc 1980440 bytes == sweep2-r19 build,
  built first-hand this seat r10).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r10 bin,
  own-seat corpus seed 4140 hardlinks + 25 fresh-oracle
  new N): RGRAMC-PYID 4165/4165 covered=4165/4165
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r10-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8330 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8330 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8330/8330
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 65109..65200: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 26/26 (13 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  a36744a (no diff on src/rgram.py, vectors/rgram-PINS.csv,
  tests/test_rgram.sh, tests/test_rgram_c.sh; 8332 PINS
  lines = 8330 + 2 header; lane diff = src/c/rgramc.c
  only, +1523/-1075).
- tables-EQ own script (tables-eq-r10.py, textual C-vs-py
  parse): NEW 10/10 EQ GREEN (S0/S1/AM/AC/BM/BC/M/QR/
  QT/QC; AC 73/BC 69/QC 63 rows = _N consts; no X26
  this tier, single-sig shape per writer record).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-676626e PASS-functional on file
  (sweep2-r19, no FLAG); CLAIM-viewer2-676626e-r10 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
