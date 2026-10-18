# VERIFY-fac36c9 cport band189 T10R134 (n<=64412, 850 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at fac36c9 under WS
  tmp/encode-viewer2/fac36c9/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD fac36c9bcc3270170a9edb3e420d25da6eb5a163
  confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/fac36c9/build-r8/rgramc
  1929880 bytes, built first-hand this seat r8).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r8 bin,
  own-seat corpus seed + fresh-oracle new pins):
  RGRAMC-PYID 4101/4101 covered=4101/4101
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r8-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8202 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8202 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-equal 8202/8202
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 64157..64412: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 22/22 (11 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + test byte-identical to parent merge d335153
  (8204 PINS lines = 8202 + 2 header; diff =
  src/c/rgramc.c only, +1220/-1061).
- tables-EQ own script (tables-eq-r8.py, textual C-vs-py
  parse): 2/2 EQ GREEN (M 16/16 + C 67/67 pairs;
  C_N=67 row-consistent). 16 T10R134 refs in rgramc.c,
  consistent with +2 tiers sealed (850).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-fac36c9 PASS-functional on file
  (sweep-r13); CLAIM-viewer2-fac36c9 oldest live verifier
  claim (field clear at claim + file time, no FLAG).

## verdict: PASS
