# REAUDIT-6436cf2 cport band102 T10P91+T10R90 (n<=48752, 670 tiers): PASS

## first-hand (fresh r14 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 6436cf2
  under WS tmp/encode-viewer3/6436cf2/tree-r14
  (seat-private, all data NVME). 5932 PINS
  lines = 5930 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/6436cf2/build-r14/
  rgramc 1467912 bytes, built first-hand
  this seat r14).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r14 bin,
  same-seat b220 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  2965/2965 covered=2965/2965 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r14-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (5930 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (5930 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 5930/5930
  (both all-PASS) + py/PINS set-eq 5930/5930.
- own-loop fresh-oracle 48405..48752: 348 pass / 0 fail
  (py+C agree all 348, rc+stdout+stderr identical);
  pins 60/60 (30 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  76fbe66 (lane diff = src/c/rgramc.c only,
  +1329/-767; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r14-b102.py, textual
  C-vs-py parse over own tree): NEW 11/11 EQ GREEN
  (P91 AC144/BC134/QC138/AM16/BM10/QM16/QT4/S0/S1 +
  R90 C128/M16) + FULL 1711/1711 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-6436cf2 PASS-functional +
  VERIFY-6436cf2 PASS + PV-6436cf2 on file (no FLAG);
  CLAIM-viewer3-6436cf2-r14 oldest live claim (field
  clear at claim + pre-filing re-check, no rival
  REAUDIT, oldest noREA down-series gap).

## verdict: PASS (concurs GATE+VERIFY+PV on every count)
