# VERIFY-08682c3 cport band208 T10P146 (n<=67636, 888 tiers): PASS

## first-hand (fresh r11 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 08682c3
  under WS tmp/encode-viewer3/08682c3/tree-r11
  (seat-private, all data NVME). 8718 PINS
  lines = 8716 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/08682c3/build-r11/
  rgramc 2049096 bytes == GATE, built
  first-hand this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus, fresh py+C execution per pin):
  RGRAMC-PYID 4358/4358 covered=4358/4358
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8716 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8716 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8716/8716
  (both all-PASS) + py/PINS set-eq 8716/8716.
- own-loop fresh-oracle 67545..67636: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  8a0fa34 (lane diff = src/c/rgramc.c only,
  +1584/-1123; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r11.py, textual C-vs-py
  parse): NEW 11/11 EQ GREEN (AC152=76x2 BC142=71x2
  QC128=64x2 + AM16 BM9 M16 QR4 QT4 S0/S1/S2),
  FULL 2427/2427 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-08682c3 PASS-functional on file
  (sweep2-r25, no FLAG); CLAIM-viewer3-08682c3-r11 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b208 merge)
