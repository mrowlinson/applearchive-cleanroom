# VERIFY-de31018 cport band83 T10P73 (n<=42168, 596 tiers): PASS

## first-hand (at-commit tree v-de31018, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  2559 union links, 0 oracle-regen): RGRAMC-PYID 2523/2523
  covered=2523/2523 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5046 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5046 pins, 0 FAIL).
- py + PINS byte-identical to parent merge b5620ea (cmp);
  diff b5620ea..de31018 = src/c/rgramc.c only (+936/-658).
- tables: 36 T10P73 refs in src/c/rgramc.c, consistent
  with +2 tiers sealed (596).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
