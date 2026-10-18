# VERIFY-711efa9 cport band210 T10P147 (n<=67984, 892 tiers): PASS

## first-hand (fresh r11 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 711efa9
  under WS tmp/encode-viewer3/711efa9/tree-r11
  (seat-private, all data NVME). 8774 PINS
  lines = 8772 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/711efa9/build-r11/
  rgramc 2066008 bytes, built first-hand
  this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus, fresh py+C execution per pin):
  RGRAMC-PYID 4386/4386 covered=4386/4386
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8772 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8772 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8772/8772
  (both all-PASS) + py/PINS set-eq 8772/8772.
- own-loop fresh-oracle 67893..67984: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  79ea6f7 (lane diff = src/c/rgramc.c only,
  +1591/-1130; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r11-b210.py, textual
  C-vs-py parse): NEW 11/11 EQ GREEN (AC148=74x2
  BC138=69x2 QC126=63x2 + AM16 BM9 M16 QR4 QT4
  S0/S1/S2), FULL 2441/2441 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-711efa9 PASS-functional on file
  (sweep2-r25, no FLAG); CLAIM-viewer3-711efa9-r11 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b210 merge)
