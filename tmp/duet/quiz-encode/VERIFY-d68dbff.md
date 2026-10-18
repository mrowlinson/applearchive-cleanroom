# VERIFY-d68dbff cport band87 T10P76+T10R75 (n<=43532, 610 tiers): PASS

## first-hand (at-commit tree v-d68dbff, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2605/2605
  covered=2605/2605 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5210 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5210 pins, 0 FAIL).
- py + PINS byte-identical to parent merge c179b2c (cmp);
  diff c179b2c..d68dbff = src/c/rgramc.c only (+1236/-676).
- tables: 67 T10P76/T10R75 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (610).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
