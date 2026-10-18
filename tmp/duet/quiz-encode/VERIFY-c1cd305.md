# VERIFY-c1cd305 cport band153 T10R116 (n<=58148, 777 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at c1cd305 under WS
  tmp/encode-viewer/c1cd305/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/c1cd305/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded 3669, 0 missing): RGRAMC-PYID 3656/3656
  covered=3656/3656 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7312 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7312 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57893..58148: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to lane base bfa3762
  (7312/7312 pins; diff = src/c/rgramc.c only,
  +1084/-943).
- tables: 14 T10R116 refs in src/c/rgramc.c,
  consistent with 3 tables added (R116).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload 0).

## verdict: PASS
