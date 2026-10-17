# VERIFY-02c66ac cport band203 T10R141 (n<=66848, 878 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 02c66ac
  under WS tmp/encode-viewer2/02c66ac/tree-r13,
  diff-identical to staged tree (diff -r rc=0,
  seat-private per PARENT-038; all data NVME
  PARENT-027). 8574 PINS lines = 8572 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/02c66ac/build-r13/
  rgramc 2015048 bytes (== r11/r12 staged), built
  first-hand this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  own-seat corpus seed + fresh-oracle new N, fresh
  py+C execution per pin): RGRAMC-PYID 4286/4286
  covered=4286/4286 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8572 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8572 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8572/8572
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 66593..66848: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  f8ad2af (lane diff = src/c/rgramc.c only,
  +1267/-1108; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M/Q len 16, C len 68,
  C _N=68).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-02c66ac PASS-functional on file
  (sweep-r16d, no FLAG); CLAIM-viewer2-02c66ac-r13 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b203 merge)
