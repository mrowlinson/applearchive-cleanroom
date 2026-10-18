# VERIFY-04cafeb cport band145 T10R112 (n<=56756, 762 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 04cafeb under WS
  tmp/encode-viewer/04cafeb/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/04cafeb/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3558/3558
  covered=3558/3558 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7116 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7116 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 56501..56756: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 64e8a0e
  (7116/7116 pins both; diff = src/c/rgramc.c only,
  +1055/-914).
- tables: 14 T10R112 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (762).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
