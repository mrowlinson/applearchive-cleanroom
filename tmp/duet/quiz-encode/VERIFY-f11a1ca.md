# VERIFY-f11a1ca cport band197 T10R138 (n<=65804, 866 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at f11a1ca under WS
  tmp/encode-viewer2/f11a1ca/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD f11a1ca confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/f11a1ca/build-r10/
  rgramc 1997416 bytes, built first-hand this seat r10).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r10 bin,
  own-seat corpus seed 4177 hardlinks + 27 fresh-oracle
  new N): RGRAMC-PYID 4204/4204 covered=4204/4204
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r10-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8408 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8408 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8408/8408
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 65549..65804: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  d9b904a (no diff on src/rgram.py, vectors/rgram-PINS.csv,
  tests/test_rgram.sh, tests/test_rgram_c.sh; 8410 PINS
  lines = 8408 + 2 header; lane diff = src/c/rgramc.c
  only, +1246/-1087).
- tables-EQ own script (tables-eq-r10.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M 16/16 + Q 16/16 C==py,
  C 69 pairs = _N const).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-f11a1ca PASS-functional on file
  (sweep-r15, no FLAG); CLAIM-viewer2-f11a1ca-r10 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
