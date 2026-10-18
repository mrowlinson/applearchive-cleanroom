# VERIFY-31e41ed cport band118 T10P101 (n<=51976, 708 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 31e41ed under WS
  tmp/encode-viewer/31e41ed/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/31e41ed/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3225/3225
  covered=3225/3225 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6450 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6450 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 51885..51976: 92 pass / 0 fail;
  pins 28/28.
- py + PINS + test byte-identical to parent merge 25c6f81
  (diff = src/c/rgramc.c only, +1267/-829).
- tables: 55 T10P101 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (708).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
