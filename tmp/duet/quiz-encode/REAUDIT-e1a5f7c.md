# REAUDIT-e1a5f7c cport band163 T10R121 (n<=59888, 798 tiers): PASS

## first-hand (at-commit tree, seat-private build)
- Tree: at-commit tree at e1a5f7c under WS
  tmp/encode-viewer/e1a5f7c-r18/tree
  (seat-private per PARENT-038; all data
  NVME PARENT-027). HEAD
  e1a5f7c037bd11c8a90ae91ea2dae83227ab6d87
  confirmed, rgramc.c cmp-identical to
  git. IN-MASTER (merged 9d29347).
- C build 0 warnings (-O2 -Wall -Wextra
  -std=c11, rc=0, own bin
  tmp/encode-viewer/e1a5f7c-r18/build/
  rgramc-r18 1809544 bytes, built
  first-hand this seat r18).
- `tests/test_rgram_c.sh` own run
  (RGRAMC=own r18 bin, own-seat corpus
  seed 4152-N hardlink ex r16, 0 fresh-
  oracle -- all 3781 N covered by seed):
  RGRAMC-PYID 3781/3781 covered=3781/
  3781 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r18-bin> tests/
  test_rgram.sh` own run: RGRAM-GREEN
  (7562 PASS, 0 FAIL, rc=0; fresh-
  oracle regen per N by script).
- `tests/test_rgram.sh` own run (py):
  RGRAM-GREEN (7562 PASS, 0 FAIL,
  rc=0; fresh-oracle regen per N).
- C/py PASS-name sets cmp-identical
  7562/7562 (both all-PASS) --
  PINS-RGRAM set-eq.
- own-loop fresh-oracle 59633..59888:
  256 pass / 0 fail (py+C agree CLOSED
  all 256, rc+stdout+stderr identical);
  pins 26/26 (13 pinned cells x closed+
  sha: 59633 59634 59647 59648 59661
  59725 59775 59776 59789 59803 59817
  59887 59888, derived from PINS
  numerically first-hand; fresh .rav
  hashes match PINS). OWNLOOP-GREEN
  rc=0.
- py + PINS + tests byte-identical to
  parent merge 06855bc (7564 PINS lines
  = 7562 + 2 header; tree diff =
  src/c/rgramc.c only, +1137/-976).
- tables-EQ own script (tables-audit-
  r18b163.py, textual C-vs-py parse):
  NEW 4/4 EQ GREEN (_T10R121C 66x2 +
  _T10R121C_N=66 row-consistent +
  _T10R121M/_T10R121QH strarr n=16);
  FULL 2132/0 (1D 166 + 2D 785 + STR
  225 + STRARR 956 incl 11 C-only
  VALS-N, all element-count consistent;
  11 _KEYS C-only out of scope per r16
  precedent). Counts concur GATE-
  e1a5f7c (incl STRARR 945 EQ + dicts
  11).
- wall-grep lane-diff (rgramc.c,
  PARENT-032 scope cpat|libcompression|
  depload|dlopen|dylib|CDLL|ctypes):
  0 hits each.
- Ordered: GATE-e1a5f7c PASS-functional
  + VERIFY-e1a5f7c PASS + merged all on
  file; CLAIM-viewer-e1a5f7c-r18 oldest
  live REAUDIT claim (field clear at
  claim + pre-filing re-check, no FLAG,
  no rival REAUDIT).

## verdict: PASS (concurs GATE + VERIFY)
