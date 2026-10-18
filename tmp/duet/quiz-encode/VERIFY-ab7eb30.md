# VERIFY-ab7eb30 cport band135 T10R107 (n<=55016, 742 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at ab7eb30 under WS
  tmp/encode-viewer/ab7eb30/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, seat bin tmp/encode-viewer/ab7eb30/build).
- `tests/test_rgram_c.sh` own run (RGRAMC=seat bin,
  corpus fresh-seeded own regen): RGRAMC-PYID 3436/3436
  covered=3436/3436 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<seat-bin> tests/test_rgram.sh` own run fresh
  oracle: RGRAM-GREEN (6872 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run fresh oracle (py):
  RGRAM-GREEN (6872 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 54761..55016: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 90ae088
  (6872/6872 pins both; diff = src/c/rgramc.c only,
  +1024/-883).
- tables: 14 T10R107 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (742).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits.

## verdict: PASS
