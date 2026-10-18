# VERIFY-6606cc1 cport band116 T10R97+T10P100 (n<=51628, 704 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 6606cc1 under WS
  tmp/encode-viewer/6606cc1/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/6606cc1/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3198/3198
  covered=3198/3198 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6396 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6396 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 51281..51628: 348 pass / 0 fail;
  pins 54/54.
- py + PINS + test byte-identical to parent merge e90d885
  (diff = src/c/rgramc.c only, +1401/-822).
- tables: 14 T10R97 + 55 T10P100 refs in src/c/rgramc.c,
  consistent with +4 tiers sealed (704).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
