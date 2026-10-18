# VERIFY-cf2775e cport band150 T10P117 (n<=57544, 772 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at cf2775e under WS
  tmp/encode-viewer/cf2775e/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/cf2775e/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3619/3619
  covered=3619/3619 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7238 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7238 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57453..57544: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 56782d2
  (7238/7238 pins both; diff = src/c/rgramc.c only,
  +1390/-930).
- tables: 60 T10P117 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (772).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
