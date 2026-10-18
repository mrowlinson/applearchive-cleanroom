# VERIFY-49f108c cport band149 T10R114 (n<=57452, 770 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 49f108c under WS
  tmp/encode-viewer/49f108c/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/49f108c/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3607/3607
  covered=3607/3607 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7214 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7214 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57197..57452: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 47e94d0
  (7214/7214 pins both; diff = src/c/rgramc.c only,
  +1070/-929).
- tables: 14 T10R114 refs in src/c/rgramc.c,
  consistent with +1 tier sealed (770).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
