# VERIFY-2333b02 cport band88 T10P77+T10R76 (n<=43880, 614 tiers): PASS

## first-hand (at-commit tree v-2333b02, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2628/2628
  covered=2628/2628 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5256 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5256 pins, 0 FAIL).
- py + PINS byte-identical to parent merge ea54647 (cmp);
  diff ea54647..2333b02 = src/c/rgramc.c only (+1271/-682).
- tables: 70 T10P77/T10R76 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (614).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
