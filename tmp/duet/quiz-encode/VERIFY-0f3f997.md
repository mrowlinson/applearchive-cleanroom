# VERIFY-0f3f997 cport band96 T10P85+T10R84 (n<=46664, 646 tiers): PASS

## first-hand (at-commit tree v-0f3f997, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2812/2812
  covered=2812/2812 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5624 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5624 pins, 0 FAIL).
- own-loop fresh-oracle 46317..46664: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge f66b1b7
  (diff = src/c/rgramc.c only, +1321/-730).
- tables: 73 T10P85/T10R84 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (646).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
