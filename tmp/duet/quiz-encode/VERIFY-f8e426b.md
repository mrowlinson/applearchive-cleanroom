# VERIFY-f8e426b cport band209 T10R144 (n<=67892, 890 tiers): PASS

## first-hand (fresh r12 export tree, seat-private build + runs)
- Tree: fresh git-archive export of f8e426b
  under WS tmp/encode-viewer3/f8e426b/tree-r12
  (seat-private, all data NVME). 8742 PINS
  lines = 8740 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/f8e426b/build-r12/
  rgramc 2049176 bytes, built first-hand
  this seat r12).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r12 bin,
  same-seat b212 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  4370/4370 covered=4370/4370 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r12-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8740 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8740 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8740/8740
  (both all-PASS) + py/PINS set-eq 8740/8740.
- own-loop fresh-oracle 67637..67892: 256 pass / 0 fail
  (py+C agree all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  ba7f71b (lane diff = src/c/rgramc.c only,
  +1288/-1129; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r12-b209.py, textual
  C-vs-py parse): NEW 3/3 EQ GREEN (C134=67x2 M16 Q16)
  + _T10R144C_N scalar 67 = C-len/2 (GATE's 4th item,
  derived-rows count, consistent); FULL 2430/2430 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-f8e426b PASS-functional + PV-f8e426b
  GREEN on file (no FLAG); CLAIM-viewer3-f8e426b-r12 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE+PV on every count; unblocks b209 merge)
