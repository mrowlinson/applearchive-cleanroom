# VERIFY-e25ae48 cport band100 T10P89+T10R88 (n<=48056, 662 tiers): PASS

## first-hand (at-commit tree vv-viewer-e25ae48, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  fresh-seeded own regen): RGRAMC-PYID 2904/2904
  covered=2904/2904 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5808 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5808 pins, 0 FAIL).
- own-loop fresh-oracle 47709..48056: 348 pass / 0 fail;
  pins 46/46.
- py + PINS + test byte-identical to parent merge 2d41980
  (diff = src/c/rgramc.c only, +1316/-754).
- tables: 69 T10P89/T10R88 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (662).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
