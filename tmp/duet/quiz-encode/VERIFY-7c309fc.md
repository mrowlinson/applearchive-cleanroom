# VERIFY-7c309fc cport band82 T10P72+T10R71 (n<=42140, 594 tiers): PASS

## first-hand (at-commit tree v-7c309fc, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038; shared path untouched).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  2559 union links, 0 oracle-regen): RGRAMC-PYID 2513/2513
  covered=2513/2513 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5026 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5026 pins, 0 FAIL).
- py + PINS byte-identical to parent merge 91f70b6 (cmp);
  diff 91f70b6..7c309fc = src/c/rgramc.c only (+1238/-652).
- tables: 70 T10P72/T10R71 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (594).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.
  (aae.c/Makefile DPAT hits OBSERVED-inherited, not in diff.)

## verdict: PASS
