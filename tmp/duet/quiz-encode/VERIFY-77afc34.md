# VERIFY-77afc34 cport band154 T10P119 (n<=58240, 778 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 77afc34 under WS
  tmp/encode-viewer/77afc34/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/77afc34/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded 3644 + fresh-oracle 25 new): RGRAMC-PYID 3669/3669
  covered=3669/3669 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7338 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7338 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 58149..58240: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to lane base 3ba738b
  (7338/7338 pins; diff = src/c/rgramc.c only,
  +1407/-944).
- tables: 60 T10P119 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (778).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload 0).

## verdict: PASS
