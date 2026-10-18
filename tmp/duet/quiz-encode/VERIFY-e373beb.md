# VERIFY-e373beb cport band140 T10P112 (n<=55804, 752 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at e373beb under WS
  tmp/encode-viewer/e373beb/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/e373beb/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3498/3498
  covered=3498/3498 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (6996 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6996 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 55713..55804: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 5e5947a
  (6996/6996 pins both; diff = src/c/rgramc.c only,
  +1348/-896).
- tables: 58 T10P112 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (752).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + libcompression 0 + depload 0, ASCII C text).

## verdict: PASS
