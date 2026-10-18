# VERIFY-18f083f cport band146 T10P115 (n<=56848, 764 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 18f083f under WS
  tmp/encode-viewer/18f083f/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/18f083f/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3571/3571
  covered=3571/3571 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7142 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7142 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 56757..56848: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 4463b37
  (7142/7142 pins both; diff = src/c/rgramc.c only,
  +1387/-915).
- tables: 65 T10P115 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (764).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
