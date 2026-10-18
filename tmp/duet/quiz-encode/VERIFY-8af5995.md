# VERIFY-8af5995 cport band143 T10R111 (n<=56408, 758 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 8af5995 under WS
  tmp/encode-viewer/8af5995/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/8af5995/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3534/3534
  covered=3534/3534 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7068 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7068 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 56153..56408: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 5741e6b
  (7068/7068 pins both; diff = src/c/rgramc.c only,
  +1047/-908).
- tables: 18 T10R111 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (758).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
