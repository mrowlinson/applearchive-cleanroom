# VERIFY-885fc37 cport band151 T10R115 (n<=57800, 774 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 885fc37 under WS
  tmp/encode-viewer/885fc37/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/885fc37/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3631/3631
  covered=3631/3631 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7262 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7262 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 57545..57800: 256 pass / 0 fail
  (py+C agree CLOSED all 256); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge a4866a6
  (7262/7262 pins both; diff = src/c/rgramc.c only,
  +1077/-936).
- tables: 14 T10R115 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (774).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT+libcompression+depload combined 0).

## verdict: PASS
