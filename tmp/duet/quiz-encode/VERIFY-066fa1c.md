# VERIFY-066fa1c cport band183 T10R131 (n<=63368, 838 tiers): PASS

## first-hand (at-commit detached worktree, seat-private build)
- Tree: detached worktree at 066fa1c under WS
  tmp/encode-viewer2/066fa1c/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 066fa1cde2b4023a9a873f325cf2bd9a329d0225
  confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/066fa1c/build/rgramc-own
  1895736 bytes, built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  corpus fresh-oracle): RGRAMC-PYID 4024/4024
  covered=4024/4024 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run: RGRAM-GREEN
  (8048 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8048 PASS, 0 FAIL, rc=0).
- own-loop fresh-oracle 63113..63368: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 20/20 (10 pinned cells x closed+sha, fresh .rav
  hashes match PINS).
- py + PINS + test byte-identical to parent merge c525c8f
  (8050 PINS lines = 8048 + 2 header; diff =
  src/c/rgramc.c only, +1180/-1039).
- tables: 16 T10R131 refs in src/c/rgramc.c,
  consistent with +2 tiers sealed (838); R-band scale
  matches b177 (15 T10R128 refs).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-066fa1c PASS-functional on file
  (sweep-r9); CLAIM-viewer2-066fa1c oldest live verifier
  claim (field clear at claim + file time).

## verdict: PASS
