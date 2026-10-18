# REAUDIT-8ecae82 cport band132 T10P108 (n<=54412, 736 tiers): PASS

## first-hand (fresh r11 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 8ecae82
  under WS tmp/encode-viewer3/8ecae82/tree-r11
  (seat-private, all data NVME). 6802 PINS
  lines = 6800 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/8ecae82/build-r11/
  rgramc 1638856 bytes, built first-hand
  this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus, fresh py+C execution per pin):
  RGRAMC-PYID 3400/3400 covered=3400/3400
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6800 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6800 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6800/6800
  (both all-PASS) + py/PINS set-eq 6800/6800.
- own-loop fresh-oracle 54321..54412: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 26/26 (13 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  f67c8a8 (lane diff = src/c/rgramc.c only,
  +1318/-874; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r11-b132.py, textual
  C-vs-py parse): NEW 10/10 EQ GREEN (AC152 BC138
  QC132 + AM16 BM10 M16 QR4 QT4 S0/S1),
  FULL 1923/1923 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Ordered: GATE-8ecae82 PASS + VERIFY-8ecae82 PASS on file,
  merged (ANCESTOR-YES); CLAIM-viewer3-8ecae82-r11 oldest
  live claim (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
