# VERIFY-0bb7583 cport band148 T10P116 (n<=57196, 768 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 0bb7583 under WS
  tmp/encode-viewer/0bb7583/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/0bb7583/work2r2/rgramc-own,
  built first-hand this seat; byte-identical to work2 bin).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3595/3595
  covered=3595/3595 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7190 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7190 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57105..57196: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge fd02d44
  (7190/7190 pins both; diff = src/c/rgramc.c only,
  +1383/-923).
- tables: 60 T10P116 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (768).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
