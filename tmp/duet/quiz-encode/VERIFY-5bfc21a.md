# VERIFY-5bfc21a cport band187 T10R133 (n<=64064, 846 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 5bfc21a under WS
  tmp/encode-viewer2/5bfc21a/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 5bfc21a873e1e925b9da397bbaebd68aca67cfed
  confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/5bfc21a/build/rgramc-own
  1929512 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  own-seat corpus seed + fresh-oracle new pins):
  RGRAMC-PYID 4076/4076 covered=4076/4076
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8152 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8152 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-equal 8152/8152
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 63809..64064: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + test byte-identical to parent merge 786f2a7
  (8154 PINS lines = 8152 + 2 header; diff =
  src/c/rgramc.c only, +1195/-1054).
- tables-EQ own script (tables-eq-r7.py, textual C-vs-py
  parse): 2/2 EQ GREEN (M 16/16 + C 70/70 pairs;
  C_N=70 row-consistent). 14 T10R133 refs in rgramc.c,
  consistent with +2 tiers sealed (846).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-5bfc21a PASS-functional on file
  (sweep-r12); CLAIM-viewer2-5bfc21a oldest live verifier
  claim (field clear at claim + file time, no FLAG).

## verdict: PASS
