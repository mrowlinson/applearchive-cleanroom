# VERIFY-c56c1e6 cport band139 T10R109 (n<=55712, 750 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at c56c1e6 under WS
  tmp/encode-viewer/c56c1e6/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/c56c1e6/build/rgramc-own).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + 12 fresh-oracle): RGRAMC-PYID 3486/3486
  covered=3486/3486 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (6972 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6972 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 55457..55712: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge c3a7a9b
  (6972/6972 pins both; diff = src/c/rgramc.c only,
  +1036/-895).
- tables: 14 T10R109 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (750).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
