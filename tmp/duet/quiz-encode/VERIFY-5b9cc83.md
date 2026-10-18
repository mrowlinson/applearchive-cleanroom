# VERIFY-5b9cc83 cport band158 T10P121 (n<=58936, 782 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 5b9cc83 under WS
  tmp/encode-viewer/5b9cc83/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/5b9cc83/work3r1/rgramc-own,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus seeded 3694 + fresh-oracle 25 new): RGRAMC-PYID 3719/3719
  covered=3719/3719 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7438 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7438 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 58845..58936: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to lane base 8e3537c
  (7438/7438 pins; diff = src/c/rgramc.c only,
  +1408/-958).
- tables: 55 T10P121 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (782).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload 0).

## verdict: PASS
