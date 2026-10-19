# REAUDIT-19ab457 cport band103 T10P92+T10B91 (n<=49100, 674 tiers): PASS

## first-hand (fresh r14 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 19ab457
  under WS tmp/encode-viewer3/19ab457/tree-r14
  (seat-private, all data NVME). 5998 PINS
  lines = 5996 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/19ab457/build-r14/
  rgramc 1484776 bytes, built first-hand
  this seat r14).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r14 bin,
  same-seat b220 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  2998/2998 covered=2998/2998 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r14-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (5996 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (5996 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 5996/5996
  (both all-PASS) + py/PINS set-eq 5996/5996.
- own-loop fresh-oracle 48753..49100: 348 pass / 0 fail
  (py+C agree all 348, rc+stdout+stderr identical);
  pins 66/66 (33 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  73df8f0 (lane diff = src/c/rgramc.c only,
  +1374/-773; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r14-b103.py, textual
  C-vs-py parse over own tree): NEW 13/13 EQ GREEN
  (P92 AC144/BC138/QC124/AM16/BM10/QM16/QR4/QT4/S0/S1 +
  B91 C128/T16/S16) + FULL 1724/1724 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-19ab457 PASS-functional +
  VERIFY-19ab457 PASS + PV-19ab457 on file (no FLAG);
  CLAIM-viewer3-19ab457-r14 oldest live claim (field
  clear at claim + pre-filing re-check, no rival
  REAUDIT, oldest noREA down-series gap).

## verdict: PASS (concurs GATE+VERIFY+PV on every count)
