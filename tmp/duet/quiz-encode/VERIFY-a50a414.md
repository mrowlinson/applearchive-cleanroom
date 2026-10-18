# VERIFY-a50a414 cport band212 T10P148 (n<=68332, 896 tiers): PASS

## first-hand (fresh r12 export tree, seat-private build + runs)
- Tree: fresh git-archive export of a50a414
  under WS tmp/encode-viewer3/a50a414/tree-r12
  (seat-private, all data NVME). 8830 PINS
  lines = 8828 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/a50a414/build-r12/
  rgramc 2066392 bytes, built first-hand
  this seat r12).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r12 bin,
  same-seat b210 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  4414/4414 covered=4414/4414 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r12-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8828 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8828 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8828/8828
  (both all-PASS) + py/PINS set-eq 8828/8828.
- own-loop fresh-oracle 68241..68332: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 32/32 (16 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  1a0d95c (lane diff = src/c/rgramc.c only,
  +1598/-1137; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r12-b212.py, textual
  C-vs-py parse): NEW 11/11 EQ GREEN (AC150=75x2
  BC142=71x2 QC128=64x2 + AM16 BM9 M16 QR4 QT4
  S0/S1/S2), FULL 2455/2455 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-a50a414 PASS-functional + PV-a50a414
  GREEN on file (no FLAG); CLAIM-viewer3-a50a414-r12 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE+PV on every count; unblocks b212 merge)
