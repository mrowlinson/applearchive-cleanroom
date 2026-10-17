# VERIFY-10a0a0f cport band202 T10P143 (n<=66592, 876 tiers): PASS

## first-hand (at-commit export tree, seat-private build)
- Tree: at-commit export of 10a0a0f under WS
  tmp/encode-viewer2/10a0a0f/tree (git archive,
  seat-private per PARENT-038; all data NVME
  PARENT-027). 8550 PINS lines = 8548 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/10a0a0f/build-r11/
  rgramc 2015000 bytes (== GATE build), built
  first-hand this seat r11).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus seed 4296 hardlinks + fresh-oracle
  new N, fresh py+C execution per pin): RGRAMC-PYID
  4274/4274 covered=4274/4274 RGRAMC-GREEN, rc=0,
  0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8548 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8548 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8548/8548
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 66501..66592: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  732dac2 (lane diff = src/c/rgramc.c only,
  +1563/-1102).
- tables-EQ own script (tables-eq-r11.py, textual C-vs-py
  parse): NEW 14/14 EQ GREEN (S0/S1/S2 + AM/AC/BM/BC/
  M/QR/QT/QC, no QS this P-row; AC _N=75, BC _N=71,
  QC _N=64).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-10a0a0f PASS-functional on file
  (sweep2-r22, no FLAG); CLAIM-viewer2-10a0a0f-r11 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count)
