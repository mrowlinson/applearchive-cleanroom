# REAUDIT-531c487 cport band134 T10P109 (n<=54760, 740 tiers): PASS

## first-hand (fresh r11 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 531c487
  under WS tmp/encode-viewer3/531c487/tree-r11
  (seat-private, all data NVME). 6850 PINS
  lines = 6848 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/531c487/build-r11/
  rgramc 1639224 bytes, built first-hand
  this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus, fresh py+C execution per pin):
  RGRAMC-PYID 3424/3424 covered=3424/3424
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6848 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6848 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6848/6848
  (both all-PASS) + py/PINS set-eq 6848/6848.
- own-loop fresh-oracle 54669..54760: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  bc5b47c (lane diff = src/c/rgramc.c only,
  +1325/-878; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r11-b134.py, textual
  C-vs-py parse): NEW 10/10 EQ GREEN (AC148 BC134
  QC132 + AM16 BM10 M16 QR4 QT4 S0/S1),
  FULL 1935/1935 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Ordered: GATE-531c487 PASS + VERIFY-531c487 PASS on file,
  merged (ANCESTOR-YES); CLAIM-viewer3-531c487-r11 oldest
  live claim (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
