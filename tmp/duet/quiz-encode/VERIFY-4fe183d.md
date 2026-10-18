# VERIFY-4fe183d cport band95 T10P84+T10R83 (n<=46316, 642 tiers): PASS

## first-hand (at-commit tree v-4fe183d, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  cumulative-seeded, 0 oracle-regen): RGRAMC-PYID 2789/2789
  covered=2789/2789 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5578 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5578 pins, 0 FAIL).
- own-loop fresh-oracle 45969..46316: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 234bf1b
  (diff = src/c/rgramc.c only, +1287/-724).
- tables: 67 T10P84/T10R83 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (642).
- wall-grep lane-diff (rgramc.c/h, PARENT-032 scope): 0 hits.

## verdict: PASS
