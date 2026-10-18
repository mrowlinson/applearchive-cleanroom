# REAUDIT-94a0e0b cport band191 T10R135 (n<=64760, 854 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 94a0e0b
  under WS tmp/encode-viewer2/94a0e0b/tree-r13,
  diff-identical to staged tree (diff -r rc=0,
  seat-private per PARENT-038; all data NVME
  PARENT-027). 8256 PINS lines = 8254 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/94a0e0b/build-r13/
  rgramc 1946744 bytes (== VERIFY build), built
  first-hand this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  own-seat corpus seed + fresh-oracle new N, fresh
  py+C execution per pin): RGRAMC-PYID 4127/4127
  covered=4127/4127 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8254 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8254 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8254/8254
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 64505..64760: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  91bdc21 (lane diff = src/c/rgramc.c only,
  +1227/-1068; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M/Q len 16, C len 67,
  C _N=67).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Backstop: GATE-94a0e0b PASS-functional (sweep-r14) +
  VERIFY-94a0e0b PASS (viewer3-r9) on file; band merged
  in master; no prior REAUDIT; CLAIM-viewer2-94a0e0b-r13
  oldest live reaudit claim (field clear at claim +
  pre-filing re-check, no rival).

## verdict: PASS (independent 2nd coverage, concurs GATE+VERIFY)
