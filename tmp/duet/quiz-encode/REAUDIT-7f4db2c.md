# REAUDIT-7f4db2c cport band165 T10R122 (n<=60236, 802 tiers): PASS

## first-hand (at-commit tree, seat-private build)
- Tree: at-commit tree at 7f4db2c under WS
  tmp/encode-viewer/7f4db2c-r17/tree
  (seat-private per PARENT-038; all data
  NVME PARENT-027). HEAD
  7f4db2c173978f642d0bab26e6a0941624d8e834
  confirmed, rgramc.c cmp-identical to
  git. IN-MASTER (merged).
- C build 0 warnings (-O2 -Wall -Wextra
  -std=c11, rc=0, own bin
  tmp/encode-viewer/7f4db2c-r17/build/
  rgramc-r17 1809880 bytes == VERIFY-
  7f4db2c build, built first-hand this
  seat r17).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r17 bin, own-seat corpus
  seed 4152-N hardlink ex r16, 0 fresh-
  oracle -- all 3807 N covered by seed):
  RGRAMC-PYID 3807/3807 covered=3807/
  3807 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r17-bin> tests/
  test_rgram.sh` own run: RGRAM-GREEN
  (7614 PASS, 0 FAIL, rc=0; fresh-
  oracle regen per N by script).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7614 PASS, 0 FAIL,
  rc=0; fresh-oracle regen per N).
- C/py PASS-name sets cmp-identical
  7614/7614 (both all-PASS) --
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 59981..60236:
  256 pass / 0 fail (py+C agree CLOSED
  all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+
  sha: 59981 59982 60031 60032 60045
  60109 60159 60160 60173 60221 60235
  60236, derived from PINS numerically
  first-hand; fresh .rav hashes match
  PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to
  parent merge 399f71d (7616 PINS lines
  = 7614 + 2 header; tree diff =
  src/c/rgramc.c only, +1123/-982).
- tables-EQ own script (tables-audit-
  r17b165.py, textual C-vs-py parse):
  NEW 3/3 EQ GREEN (_T10R122M strarr
  n=16 + _T10R122C 68x2 + _T10R122C_N=
  68 row-consistent); FULL 2144/0 (1D
  166 + 2D 789 + STR 227 + STRARR 962
  incl 11 C-only VALS-N, all element-
  count consistent; 11 _KEYS C-only out
  of scope per r16 precedent). Counts
  concur GATE-7f4db2c (incl STRARR
  951 EQ + dicts 11).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|libcompression|
  depload|dlopen|dylib|CDLL|ctypes):
  0 hits each.
- Ordered: GATE-7f4db2c PASS-functional
  + VERIFY-7f4db2c PASS + merged all on
  file; CLAIM-viewer-7f4db2c-r17 oldest
  live REAUDIT claim (field clear at
  claim + pre-filing re-check, no FLAG,
  no rival REAUDIT).

## verdict: PASS (concurs GATE + VERIFY)
