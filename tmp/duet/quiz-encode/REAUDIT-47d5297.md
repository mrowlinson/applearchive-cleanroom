# REAUDIT-47d5297 cport band128 T10P106 (n<=53716, 728 tiers): PASS

## first-hand (fresh r12 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 47d5297
  under WS tmp/encode-viewer3/47d5297/tree-r12
  (seat-private, all data NVME). 6702 PINS
  lines = 6700 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/47d5297/build-r12/
  rgramc 1621672 bytes, built first-hand
  this seat r12).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r12 bin,
  same-seat corpus seed + missing-only fresh-oracle regen,
  fresh py+C execution per pin): RGRAMC-PYID 3350/3350
  covered=3350/3350 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r12-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6700 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6700 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6700/6700
  (both all-PASS) + py/PINS set-eq 6700/6700.
- own-loop fresh-oracle 53625..53716: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 26/26 (13 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  84785e0 (lane diff = src/c/rgramc.c only,
  +1316/-859; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r12-b128.py, textual
  C-vs-py parse): NEW 11/11 EQ GREEN (AC152 BC136
  QC130 + AM16 BM9 M16 QR4 QT4 S0/S1 BS1),
  FULL 1899/1899 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Ordered: GATE-47d5297 PASS + VERIFY-47d5297 PASS + PV merged
  0b394a5 on file; CLAIM-viewer3-47d5297-r12 oldest
  live claim (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
