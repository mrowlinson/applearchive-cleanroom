# VERIFY-9afecce cport band174 T10P129 (n<=61720, 820 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 9afecce under WS
  tmp/encode-viewer2/9afecce/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/9afecce/build/rgramc-own
  1861176 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 3915/3915
  covered=3915/3915 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (7830 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (7830 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 61629..61720: 92 pass / 0 fail
  (py+C agree CLOSED all 92); pins 26/26 (13 pinned
  cells x closed+sha, fresh .rav hashes match).
- py + PINS + test byte-identical to parent merge bd77131
  (7832/7832 lines both; diff = src/c/rgramc.c only,
  +1470/-1007).
- tables: 60 T10P129 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (820).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope): 0 hits
  (CPAT 0 + LIBCOMPRESSION 0 + depload/dlopen/dylib 0).

## verdict: PASS
