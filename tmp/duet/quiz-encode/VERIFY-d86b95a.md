# VERIFY-d86b95a cport band141 T10R110 (n<=56060, 754 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at d86b95a under WS
  tmp/encode-viewer/d86b95a/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/d86b95a/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3510/3510
  covered=3510/3510 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7020 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7020 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 55805..56060: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge ef02d89
  (7020/7020 pins both; diff = src/c/rgramc.c only,
  +1062/-901).
- tables: 17 T10R110 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (754).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
