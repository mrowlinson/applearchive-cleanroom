# VERIFY-43b0519 cport band93 T10P82+T10R81 (n<=45620, 634 tiers): PASS

## first-hand (at-commit tree v-43b0519, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2743/2743
  covered=2743/2743 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5486 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5486 pins, 0 FAIL).
- own-loop fresh-oracle 45273..45620: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 235f271
  (diff = src/c/rgramc.c only, +1274/-712).
- tables: 67 T10P82/T10R81 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (634).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
