# VERIFY-cf229ce cport band219 T10R149 (n<=69632, 910 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of cf229ce
  under WS tmp/encode-viewer3/cf229ce/tree-r13
  (seat-private, all data NVME). 9022 PINS
  lines = 9020 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/cf229ce/build-r13/
  rgramc 2100488 bytes, built first-hand
  this seat r13; == GATE's byte count).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  same-seat b217 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  4510/4510 covered=4510/4510 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (9020 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (9020 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 9020/9020
  (both all-PASS) + py/PINS set-eq 9020/9020.
- own-loop fresh-oracle 69377..69632: 256 pass / 0 fail
  (py+C agree all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  4b9fe8e (lane diff = src/c/rgramc.c only,
  +1321/-1162; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13-b219.py, textual
  C-vs-py parse over own tree): NEW 3/3 EQ GREEN
  (C134=67x2 M16 Q16; GATE's 4th item = _N=67
  derived-rows scalar, consistent) + FULL
  2498/2498 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-cf229ce PASS-functional
  on file (no FLAG, no PV yet); CLAIM-viewer3-cf229ce-r13
  oldest live verifier claim (field clear at claim +
  pre-filing re-check: GATE + spent gate-prod +
  own claim only; no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b219 merge)
