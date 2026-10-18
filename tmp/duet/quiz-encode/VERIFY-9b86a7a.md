# VERIFY-9b86a7a cport band217 T10R148 (n<=69284, 906 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 9b86a7a
  under WS tmp/encode-viewer3/9b86a7a/tree-r13
  (seat-private, all data NVME). 8966 PINS
  lines = 8964 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/9b86a7a/build-r13/
  rgramc 2100168 bytes, built first-hand
  this seat r13; == GATE's byte count).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  same-seat b209 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  4482/4482 covered=4482/4482 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8964 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8964 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8964/8964
  (both all-PASS) + py/PINS set-eq 8964/8964.
- own-loop fresh-oracle 69029..69284: 256 pass / 0 fail
  (py+C agree all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  3f397ee (lane diff = src/c/rgramc.c only,
  +1315/-1156; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13-b217.py, textual
  C-vs-py parse over own tree): NEW 3/3 EQ GREEN
  (C138=69x2 M16 Q16; GATE's 4th item = _N=69
  derived-rows scalar, consistent) + FULL
  2485/2485 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-9b86a7a PASS-functional
  on file (no FLAG, no PV yet); CLAIM-viewer3-9b86a7a-r13
  oldest live verifier claim (field clear at claim +
  pre-filing re-check: GATE + spent gate-prod +
  own claim only; no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b217 merge)
