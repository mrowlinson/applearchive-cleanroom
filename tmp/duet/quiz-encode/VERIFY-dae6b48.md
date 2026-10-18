# VERIFY-dae6b48 cport band152 T10P118 (n<=57892, 776 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at dae6b48 under WS
  tmp/encode-viewer/dae6b48/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/dae6b48/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3644/3644
  covered=3644/3644 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7288 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7288 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57801..57892: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge d497e00
  (7288/7288 pins both; diff = src/c/rgramc.c only,
  +1400/-937).
- tables: 60 T10P118 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (776).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
