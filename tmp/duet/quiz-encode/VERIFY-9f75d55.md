# VERIFY-9f75d55 cport band144 T10P114 (n<=56500, 760 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 9f75d55 under WS
  tmp/encode-viewer/9f75d55/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/9f75d55/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3546/3546
  covered=3546/3546 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7092 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7092 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 56409..56500: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 6e9422a
  (7092/7092 pins both; diff = src/c/rgramc.c only,
  +1355/-911).
- tables: 55 T10P114 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (760).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
