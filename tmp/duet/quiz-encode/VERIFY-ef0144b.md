# VERIFY-ef0144b cport band193 T10R136 (n<=65108, 858 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at ef0144b under WS
  tmp/encode-viewer/ef0144b-r16/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD ef0144be772c04155f62403dfb10351ad4f0cf54
  confirmed, rgramc.c cmp-identical to git.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer/ef0144b-r16/
  build/rgramc-r16 1947128 bytes, built
  first-hand this seat r16).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r16 bin,
  own-seat corpus seed 4101 .rav hardlink ex r15 +
  fresh-oracle new N): RGRAMC-PYID 4152/4152
  covered=4152/4152 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r16-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8304 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8304 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-equal 8304/8304
  (both all-PASS) -- PINS-RGRAM set-eq.
- own-loop fresh-oracle 64853..65108: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS; expect 12x2 derived from PINS
  numerically first-hand). OWNLOOP-GREEN rc=0.
- py + PINS + test byte-identical to parent merge ad52ea0
  (8306 PINS lines = 8304 + 2 header; diff =
  src/c/rgramc.c only, +1233/-1074).
- tables-EQ own script (tables-audit-r16b193.py, textual
  C-vs-py parse): NEW 2/2 EQ GREEN (_T10R136C 66/66
  pairs + _T10R136C_N=66 row-consistent); FULL 1275/0
  (1D 167 + 2D 845 + STR 263; 11 _KEYS C-only out
  of scope).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib|CDLL|ctypes):
  0 hits each.
- GATE-first ordered: GATE-ef0144b PASS-functional on file
  (sweep-r14; lane-diff +1233/-1074 + range 64853..65108
  concur); CLAIM-viewer-ef0144b-r16 oldest live verifier
  claim (field clear at claim + file time, no FLAG).

## verdict: PASS
