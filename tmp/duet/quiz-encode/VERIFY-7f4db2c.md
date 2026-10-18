# VERIFY-7f4db2c cport band165 T10R122 (n<=60236, 802 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 7f4db2c under WS
  tmp/encode-viewer2/7f4db2c/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/7f4db2c/build/rgramc-own
  1809880 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 3807/3807
  covered=3807/3807 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7614 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7614 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 59981..60236: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 399f71d
  (7616/7616 lines both; diff = src/c/rgramc.c only,
  +1123/-982).
- tables: 14 T10R122 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (802).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload/dlopen/dylib 0).

## verdict: PASS
