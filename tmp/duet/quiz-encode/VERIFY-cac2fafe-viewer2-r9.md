# VERIFY-cac2fafe-viewer2-r9: cport band68 T10R60+T10P62 (n<=38340, 552 tiers) — PASS
(second independent first-hand battery; VERIFY-cac2faf (Oct 9) stands —
this seat's pre-claim scan missed its 7-char stem. Filed suffixed per
PARENT-071 / d1a3c2d precedent. Numbers concur on every leg.)

## first-hand (at-commit detached tree, seat-private build)
- Tree: WS tmp/encode-viewer2/cac2fafe/tree,
  detached HEAD cac2fafe confirmed, status clean.
  (Seat-private per PARENT-038; all data NVME PARENT-027.)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/cac2fafe/build-r9/rgramc
  1178024 bytes, built first-hand this seat r9).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r9 bin,
  own-seat corpus seed 2276/2276 hardlinks, 0 oracle regen):
  RGRAMC-PYID 2276/2276 covered=2276/2276
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r9-bin> tests/test_rgram.sh` own run
  (fresh oracle per cell): RGRAM-GREEN
  (4552 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py, fresh oracle):
  RGRAM-GREEN (4552 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 4552/4552
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 37993..38340 (R60A off=0 ..
  P62B top): 348 pass / 0 fail (py+C agree CLOSED
  all 348, rc+stdout+stderr identical); pins 20x2 =
  40/40 (fresh .rav sha match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to parent merge
  57108c8 (cmp SAME on rgram.py, PINS, both test
  scripts; 4554 PINS lines = 4552 + 2 header; diff =
  src/c/rgramc.c only, +1150/-590).
- tables-EQ own script (tables-eq-r9.py, textual C-vs-py
  parse): 11/11 EQ GREEN (R60 AM16/AQ4/AC61/BM16/BC66 +
  P62 S0/S1 160ch + AM16/AC71/BM10/BC67; _N 61/66/71/67
  row-consistent).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib|CPAT): 0 hits.
- GATE-first ordered: GATE-cac2fafe PASS-functional on file;
  CLAIM-viewer2-cac2fafe oldest live verifier claim
  (field clear at claim + file time, no FLAG).

## verdict: PASS
