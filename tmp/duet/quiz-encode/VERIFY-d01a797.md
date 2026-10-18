# VERIFY-d01a797 cport band207 T10R143 (n<=67544, 886 tiers): PASS

## first-hand (fresh r13 export tree, seat-private build + runs)
- Tree: fresh git-archive export of d01a797
  under WS tmp/encode-viewer2/d01a797/tree-r13
  (seat-private per PARENT-038; all data NVME
  PARENT-027). 8686 PINS lines = 8684 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/d01a797/build-r13/
  rgramc 2048792 bytes, built first-hand this seat r13).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r13 bin,
  own-seat corpus seed chained 4408 ex own b205 r13 +
  missing-only fresh-oracle regen, fresh py+C execution
  per pin): RGRAMC-PYID 4342/4342 covered=4342/4342
  RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r13-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8684 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8684 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8684/8684
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 67289..67544: 256 pass / 0 fail
  (py+C agree CLOSED all 256, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  a86038d (lane diff = src/c/rgramc.c only,
  +1281/-1122; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r13.py, textual C-vs-py
  parse): NEW 3/3 EQ GREEN (M/Q len 16, C len 69,
  C _N=69).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- GATE-first ordered: GATE-d01a797 PASS-functional on file
  (sweep-r16e, no FLAG); CLAIM-viewer2-d01a797-r13 oldest
  live verifier claim (field clear at claim + pre-filing
  re-check, no rival VERIFY).

## verdict: PASS (concurs GATE on every count; unblocks b207 merge)
