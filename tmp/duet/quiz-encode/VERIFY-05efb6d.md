# VERIFY-05efb6d cport band190 T10P137 (n<=64504, 852 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 05efb6d under WS
  tmp/encode-viewer3/05efb6d/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 05efb6db236ab1729e80b1c6f2eebefe2234912d
  confirmed, status clean.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/05efb6d/build/
  rgramc-r8 1946696 bytes == sweep2-r17 build,
  built first-hand this seat).
- `tests/test_rgram_c.sh` own run (RGRAMC=own bin,
  own-seat corpus seed + fresh-oracle new pins):
  RGRAMC-PYID 4115/4115 covered=4115/4115
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8230 PASS, 0 FAIL, log GREEN).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8230 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-equal 8230/8230
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 64413..64504: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 28/28 (14 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  8079ebb (no diff on src/rgram.py, vectors/rgram-PINS.csv,
  tests/test_rgram.sh, tests/test_rgram_c.sh; 8232 PINS
  lines = 8230 + 2 header; lane diff = src/c/rgramc.c
  only, +1523/-1062).
- tables-EQ own script (tables-eq-v3.py, textual C-vs-py
  parse): NEW 11/11 EQ GREEN (AC/BC/QC/AM/BM/M/QR/QT/
  S0/S1/S2) + FULL 2301/2301 0-skip 0-mismatch.
  60 T10P137 refs (31 _T10P137 tables) in rgramc.c,
  consistent with +2 tiers sealed (852).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-05efb6d PASS-functional on file
  (sweep2-r17); CLAIM-viewer3-05efb6d oldest live verifier
  claim (field clear at claim + file time, no FLAG, no
  rival VERIFY).

## verdict: PASS
