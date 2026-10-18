# VERIFY-a6e4edc cport band89 T10P78+T10R77 (n<=44228, 618 tiers): PASS

## first-hand (at-commit tree v-a6e4edc, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2651/2651
  covered=2651/2651 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5302 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5302 pins, 0 FAIL).
- py + PINS byte-identical to parent merge 196de79 (cmp);
  diff 196de79..a6e4edc = src/c/rgramc.c only (+1250/-688).
- tables: 67 T10P78/T10R77 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (618).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
