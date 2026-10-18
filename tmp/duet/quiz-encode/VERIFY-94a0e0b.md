# VERIFY-94a0e0b cport band191 T10R135 (n<=64760, 854 tiers): PASS

## first-hand (at-commit detached tree, seat-private build)
- Tree: detached tree at 94a0e0b under WS
  tmp/encode-viewer3/94a0e0b/tree (seat-private
  per PARENT-038; all data NVME PARENT-027).
  HEAD 94a0e0b58f55134bd31bc1ffd8b2bba11245c5a8
  confirmed, status clean (r9 recheck).
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/94a0e0b/build/
  rgramc-r9 1946744 bytes == r8 size; 49 bytes
  differ = LC_UUID random-per-link (dwarfdump-
  confirmed) + output-path string only;
  rebuilt + verified first-hand this round).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r9
  bin, seeded corpus, all 4127 py+C freshly
  executed): RGRAMC-PYID 4127/4127
  covered=4127/4127 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-bin> tests/test_rgram.sh` r8 run
  adopted after first-hand log verification:
  RGRAM-GREEN (8254 PASS, 0 FAIL); `tests/
  test_rgram.sh` (py): RGRAM-GREEN (8254 PASS,
  0 FAIL). Logs fresh (<2h), counts rechecked
  by r9 (grep PASS/FAIL + GREEN tails).
- C/py PASS-name sets cmp-equal 8254/8254
  (both all-PASS) — PINS-RGRAM set-eq (r9
  cmp recheck).
- Spot re-run FRESH-oracle r9 (spot-r9.sh, r9
  binary, 24 N incl. band edges 64505/64760):
  24/24 py-vs-C identical (rc+stdout+stderr),
  pins 18/18 (closed+sha), SPOT-GREEN rc=0.
- own-loop fresh-oracle 64505..64760 r8 run
  adopted after first-hand log verification:
  256 pass / 0 fail, pins 24/24, OWNLOOP-GREEN
  rc=0 (fresh <2h; band edges re-covered by r9
  fresh spot above).
- py + PINS + tests byte-identical to writer-merge
  parent 91bdc21 (no diff on src/rgram.py,
  vectors/rgram-PINS.csv, tests/test_rgram.sh,
  tests/test_rgram_c.sh; 8256 PINS lines =
  8254 + 2 header; lane diff = src/c/rgramc.c
  only, +1227/-1068; r9 recheck).
- tables-EQ own script (tables-eq-v3.py, textual
  C-vs-py parse), FRESH r9 run: NEW 3/3 EQ
  (_T10R135C/M/Q) + FULL 2304/2304 0-skip
  0-mismatch, rc=0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib):
  0 hits (r9 recheck).
- GATE-first ordered: GATE-94a0e0b PASS-functional
  on file (sweep-r14); CLAIM-viewer3-94a0e0b
  oldest live verifier claim (field clear at
  claim + file time, no FLAG, no rival VERIFY;
  PARENT-071 claim-check done).

## verdict: PASS
