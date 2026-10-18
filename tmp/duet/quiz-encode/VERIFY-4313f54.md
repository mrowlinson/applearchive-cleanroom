# VERIFY-4313f54 cport band171 T10R125 (n<=61280, 814 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 4313f54 under WS
  tmp/encode-viewer2/4313f54/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/4313f54/build/rgramc-own
  1843896 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 3877/3877
  covered=3877/3877 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7754 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7754 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 61025..61280: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 48a1ad0
  (7756/7756 lines both; diff = src/c/rgramc.c only,
  +1141/-1000).
- tables: 14 T10R125 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (814).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload/dlopen/dylib 0).

## verdict: PASS
