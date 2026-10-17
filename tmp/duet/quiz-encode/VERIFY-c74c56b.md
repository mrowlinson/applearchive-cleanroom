# VERIFY-c74c56b cport band201 T10R140 (n<=66500, 874 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of c74c56b under WS
  tmp/encode-viewer2/c74c56b/tree (git archive,
  seat-private per PARENT-038; all data NVME
  PARENT-027). 8518 PINS lines = 8516 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/c74c56b/build-r11/
  rgramc 2014680 bytes, built first-hand this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus seed 4244 hardlinks + fresh-oracle
  new N, fresh py+C execution per pin): RGRAMC-PYID
  4258/4258 covered=4258/4258 RGRAMC-GREEN, rc=0,
  0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8516 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8516 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8516/8516
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 66245..66500: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  1177b26 (lane diff = src/c/rgramc.c only,
  +1260/-1101).
- tables-EQ own script (tables-eq-r11.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M 16/16, Q 16/16,
  C 69 pairs; C _N=69 derived).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-c74c56b PASS-functional on file
  (sweep-r16c, no FLAG); CLAIM-viewer2-c74c56b-r11 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
