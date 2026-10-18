# REAUDIT-4798cde cport band101 T10P90+T10R89 (n<=48404, 666 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 4798cde
  under WS tmp/encode-viewer3/4798cde/tree-r13
  (seat-private, all data NVME). 5872 PINS
  lines = 5870 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/4798cde/build-r13/
  rgramc 1451112 bytes, built first-hand
  this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  same-seat b100 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  2935/2935 covered=2935/2935 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (5870 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (5870 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 5870/5870
  (both all-PASS) + py/PINS set-eq 5870/5870.
- own-loop fresh-oracle 48057..48404: 348 pass / 0 fail
  (py+C agree all 348, rc+stdout+stderr identical);
  pins 62/62 (31 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  174f8a4 (lane diff = src/c/rgramc.c only,
  +1365/-760; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13-b101.py, textual
  C-vs-py parse over own tree): NEW 14/14 EQ GREEN
  (P90 AC146/BC136/QC120/AM16/BM9/QM16/QR4/QT4/
  S0/S1/SS + R89 C128/M16/Q16, == GATE's 14) +
  FULL 1700/1700 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-4798cde PASS-functional +
  VERIFY-4798cde PASS + PV-4798cde on file (no FLAG);
  CLAIM-viewer3-4798cde-r13 oldest live claim (field
  clear at claim + pre-filing re-check, no rival
  REAUDIT, oldest noREA down-series gap).

## verdict: PASS (concurs GATE+VERIFY+PV on every count)
