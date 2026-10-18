# REAUDIT-e25ae48 cport band100 T10P89+T10R88 (n<=48056, 662 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of e25ae48
  under WS tmp/encode-viewer3/e25ae48/tree-r13
  (seat-private, all data NVME). 5810 PINS
  lines = 5808 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/e25ae48/build-r13/
  rgramc 1450728 bytes, built first-hand
  this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  same-seat f8e426b corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  2904/2904 covered=2904/2904 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (5808 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (5808 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 5808/5808
  (both all-PASS) + py/PINS set-eq 5808/5808.
- own-loop fresh-oracle 47709..48056: 348 pass / 0 fail
  (py+C agree all 348, rc+stdout+stderr identical);
  pins 46/46 (23 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  2d41980 (lane diff = src/c/rgramc.c only,
  +1316/-754; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13-b100.py, textual
  C-vs-py parse over own tree): NEW 11/11 EQ GREEN
  (P89 AC142/BC138/AM16/BM10/S0/S1 + R88
  AC120/BC126/AM16/AQ4/BM16, == GATE's 11) +
  FULL 1686/1686 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-e25ae48 PASS-functional +
  VERIFY-e25ae48 PASS + PV-e25ae48 on file (no FLAG);
  CLAIM-viewer3-e25ae48-r13 oldest live claim (field
  clear at claim + pre-filing re-check, no rival
  REAUDIT, oldest noREA down-series gap).

## verdict: PASS (concurs GATE+VERIFY+PV on every count)
