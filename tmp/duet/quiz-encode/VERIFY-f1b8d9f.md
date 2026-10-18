# VERIFY-f1b8d9f cport band220 T10P152 (n<=69724, 912 tiers): PASS

## first-hand (fresh r14 export tree, seat-private build + runs)
- Tree: fresh git-archive export of f1b8d9f
  under WS tmp/encode-viewer3/f1b8d9f/tree-r14
  (seat-private, all data NVME). 9054 PINS
  lines = 9052 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/f1b8d9f/build-r14/
  rgramc 2117320 bytes, built first-hand
  this seat r14; == GATE's byte count).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r14 bin,
  same-seat b219 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  4526/4526 covered=4526/4526 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r14-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (9052 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (9052 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 9052/9052
  (both all-PASS) + py/PINS set-eq 9052/9052.
- own-loop fresh-oracle 69633..69724: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  d903ab7 (lane diff = src/c/rgramc.c only,
  +1624/-1163; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r14-b220.py, textual
  C-vs-py parse over own tree): NEW 11/11 EQ GREEN
  (AC150=75x2 BC142=71x2 QC126=63x2 == GATE's 3 rows
  + 8 smalls AM16/BM9/M16/QR4/QT4/S0/S1/S2) +
  FULL 2509/2509 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-f1b8d9f PASS-functional
  on file (no FLAG, no PV yet); CLAIM-viewer3-f1b8d9f-r14
  oldest live verifier claim (field clear at claim +
  pre-filing re-check: GATE + spent gate-prod +
  own claim only; no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b220 merge)
