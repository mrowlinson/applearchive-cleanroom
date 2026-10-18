# VERIFY-9d9b10d cport band199 T10R139 (n<=66152, 870 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 9d9b10d under WS
  tmp/encode-viewer2/9d9b10d/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 9d9b10d confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/9d9b10d/build-r11/
  rgramc 1997784 bytes, built first-hand this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus seed 4244 hardlinks, fresh py+C
  execution per pin): RGRAMC-PYID 4232/4232
  covered=4232/4232 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8464 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8464 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8464/8464
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 65897..66152: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  643d5cd (lane diff = src/c/rgramc.c only,
  +1253/-1094; 8466 PINS lines = 8464 + 2 header).
- tables-EQ own script (tables-eq-r11.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M 16/16, Q 16/16,
  C 68 pairs; C _N=68 derived).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-9d9b10d PASS-functional on file
  (sweep-r16c, no FLAG); CLAIM-viewer2-9d9b10d-r11 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
