# VERIFY-c91ee06 cport band137 T10R108 (n<=55364, 746 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at c91ee06 under WS
  tmp/encode-viewer/c91ee06/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/c91ee06/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3461/3461
  covered=3461/3461 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6922 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6922 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 55109..55364: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 2aec499
  (6922/6922 pins both; diff = src/c/rgramc.c only,
  +1030/-889).
- tables: 14 T10R108 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (746).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
