# VERIFY-f01b41d cport band168 T10P126 (n<=60676, 808 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at f01b41d under WS
  tmp/encode-viewer2/f01b41d/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/f01b41d/build/rgramc-own
  1827000 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 3843/3843
  covered=3843/3843 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7686 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7686 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 60585..60676: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 24/24 (12 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge 5314e97
  (7688/7688 lines both; diff = src/c/rgramc.c only,
  +1439/-989).
- tables: 55 T10P126 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (808).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload/dlopen/dylib 0).

## verdict: PASS
