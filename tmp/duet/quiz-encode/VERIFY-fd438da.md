# VERIFY-fd438da cport band147 T10R113 (n<=57104, 766 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at fd438da under WS
  tmp/encode-viewer/fd438da/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  own bin tmp/encode-viewer/fd438da/work2/rgramc-own,
  seat record pre-compaction; binary + all logs
  below read first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded + fresh-oracle for missing): RGRAMC-PYID 3583/3583
  covered=3583/3583 RGRAMC-GREEN, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7166 PASS, 0 FAIL; tail g-z57104).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7166 PASS, 0 FAIL; tail g-z57104).
- own-loop fresh-oracle 56849..57104: pass=256 fail=0
  pins=12 pinfail=0, OWN-GREEN (12 pinned cells =
  24/24 closed+sha checks).
- py + PINS + test byte-identical to parent merge cddf1f3
  per GATE-fd438da lane-diff (diff = src/c/rgramc.c only,
  +1083/-922; second-hand, labeled).
- tables: 18 T10R113 refs in src/c/rgramc.c (M/QH/C
  tables + C_N=66 + decoder legs), consistent with +2
  tiers sealed (766); full table audit per GATE 4/4 EQ.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (seat record pre-compaction; GATE confirms 0).

## verdict: PASS
