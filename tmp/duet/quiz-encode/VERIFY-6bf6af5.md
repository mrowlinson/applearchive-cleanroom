# VERIFY-6bf6af5 cport band198 T10P141 (n<=65896, 868 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 6bf6af5 under WS
  tmp/encode-viewer2/6bf6af5/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 6bf6af5 confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/6bf6af5/build-r10/
  rgramc 1997720 bytes, built first-hand this seat r10).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r10 bin,
  own-seat corpus seed 4204 hardlinks + 16 fresh-oracle
  new N): RGRAMC-PYID 4220/4220 covered=4220/4220
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r10-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8440 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8440 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8440/8440
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 65805..65896: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  5215124 (no diff on src/rgram.py, vectors/rgram-PINS.csv,
  tests/test_rgram.sh, tests/test_rgram_c.sh; 8442 PINS
  lines = 8440 + 2 header; lane diff = src/c/rgramc.c
  only, +1549/-1088).
- tables-EQ own script (tables-eq-r10.py, textual C-vs-py
  parse): NEW 11/11 EQ GREEN (S0/S1/S2/AM/AC/BM/BC/M/
  QR/QT/QC; AC 73/BC 69/QC 62 rows = _N consts).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-6bf6af5 PASS-functional on file
  (sweep2-r20, no FLAG); CLAIM-viewer2-6bf6af5-r10 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
