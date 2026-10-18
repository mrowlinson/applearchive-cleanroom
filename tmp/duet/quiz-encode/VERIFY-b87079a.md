# VERIFY-b87079a cport band138 T10P111 (n<=55456, 748 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at b87079a under WS
  tmp/encode-viewer/b87079a/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/b87079a/build/rgramc-own;
  functionally identical to staged bin on spot probe).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + 13 fresh-oracle): RGRAMC-PYID 3474/3474
  covered=3474/3474 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (6948 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6948 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 55365..55456: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge e5b435f
  (6948/6948 pins both; diff = src/c/rgramc.c only,
  +1336/-890).
- tables: 55 T10P111 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (748).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
