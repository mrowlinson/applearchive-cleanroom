# VERIFY-bf2d330 cport band142 T10P113 (n<=56152, 756 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at bf2d330 under WS
  tmp/encode-viewer/bf2d330/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/bf2d330/work2/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3522/3522
  covered=3522/3522 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7044 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7044 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 56061..56152: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 188be03
  (7044/7044 pins both; diff = src/c/rgramc.c only,
  +1361/-902).
- tables: 60 T10P113 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (756).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
