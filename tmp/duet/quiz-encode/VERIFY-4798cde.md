# VERIFY-4798cde cport band101 T10P90+T10R89 (n<=48404, 666 tiers): PASS

## first-hand (at-commit tree vv-viewer-4798cde, seat-private build)
- C build 0 warnings (-O2 -Wall -Wextra -std=c11, BUILDDIR
  seat-private per PARENT-038).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin, corpus
  fresh-seeded own regen): RGRAMC-PYID 2935/2935
  covered=2935/2935 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (5870 pins, 0 FAIL).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (5870 pins, 0 FAIL).
- own-loop fresh-oracle 48057..48404: 348 pass / 0 fail;
  pins 62/62.
- py + PINS + test byte-identical to parent merge 174f8a4
  (diff = src/c/rgramc.c only, +1365/-760).
- tables: 90 T10P90/T10R89 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (666).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
