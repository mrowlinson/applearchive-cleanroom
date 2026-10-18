# VERIFY-8b26a1f cport band205 T10R142 (n<=67196, 882 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 8b26a1f
  under WS tmp/encode-viewer2/8b26a1f/tree-r13
  (seat-private per PARENT-038; all data NVME
  PARENT-027). 8630 PINS lines = 8628 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/8b26a1f/build-r13/
  rgramc 2031896 bytes, built first-hand this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  own-seat corpus seed chained 4352 ex own b203 r13 +
  missing-only fresh-oracle regen, fresh py+C execution
  per pin): RGRAMC-PYID 4314/4314 covered=4314/4314
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8628 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8628 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8628/8628
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 66941..67196: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  150ba00 (lane diff = src/c/rgramc.c only,
  +1273/-1114; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M/Q len 16, C len 67,
  C _N=67).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-8b26a1f PASS-functional on file
  (sweep-r16e, no FLAG); CLAIM-viewer2-8b26a1f-r13 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b205 merge)
