# VERIFY-bd1ca6d cport band192 T10P138 (n<=64852, 856 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at bd1ca6d under WS
  tmp/encode-viewer2/bd1ca6d/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD bd1ca6d confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/bd1ca6d/build-r10/
  rgramc 1947048 bytes == sweep2-r19 build,
  built first-hand this seat r10).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r10 bin,
  own-seat corpus seed 4115 hardlinks + 25 fresh-oracle
  new N): RGRAMC-PYID 4140/4140 covered=4140/4140
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r10-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8280 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8280 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8280/8280
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 64761..64852: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 26/26 (13 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  eec085d (no diff on src/rgram.py, vectors/rgram-PINS.csv,
  tests/test_rgram.sh, tests/test_rgram_c.sh; 8282 PINS
  lines = 8280 + 2 header; lane diff = src/c/rgramc.c
  only, +1520/-1069).
- tables-EQ own script (tables-eq-r10.py, textual C-vs-py
  parse): NEW 11/11 EQ GREEN (S0/S1/AM/AC/BM/BC/M/X26/
  QR/QT/QC; X26 16/16 bytes C-decimal == py-hex; AC 77/
  BC 71/QC 63 rows = _N consts).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-bd1ca6d PASS-functional on file
  (sweep2-r19, no FLAG); CLAIM-viewer2-bd1ca6d-r10 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
