# VERIFY-f341d1b cport band92 T10P81+T10R80 (n<=45272, 630 tiers): PASS

## first-hand (at-commit tree v-f341d1b, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2720/2720
  covered=2720/2720 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5440 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5440 pins, 0 FAIL).
- own-loop fresh-oracle 44925..45272: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 6cc4588
  (diff = src/c/rgramc.c only, +1268/-706).
- tables: 77 T10P81/T10R80 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (630).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
