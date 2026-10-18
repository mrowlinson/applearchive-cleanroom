# VERIFY-fe4c199 cport band177 T10R128 (n<=62324, 826 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at fe4c199 under WS
  tmp/encode-viewer2/fe4c199/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/fe4c199/build/rgramc-own
  1878104 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 3950/3950
  covered=3950/3950 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7900 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7900 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 62069..62324: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 2479628
  (7902/7902 PINS lines; diff = src/c/rgramc.c only,
  +1166/-1019).
- tables: 15 T10R128 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (826).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload/dlopen/dylib 0).

## verdict: PASS
