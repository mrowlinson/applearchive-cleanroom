# REAUDIT-12b8957 cport band122 T10P103 (n<=52672, 716 tiers): PASS

## first-hand (fresh r14 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 12b8957
  under WS tmp/encode-viewer2/12b8957/tree-r14
  (seat-private per PARENT-038; all data NVME
  PARENT-027). 6552 PINS lines = 6550 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/12b8957/build-r14/
  rgramc 1587624 bytes, built first-hand this seat r14).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r14 bin,
  own-seat corpus seed 4464 ex d01a797 r13 + fresh-oracle
  missing-only, fresh py+C execution per pin):
  RGRAMC-PYID 3275/3275 covered=3275/3275 RGRAMC-GREEN,
  rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r14-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6550 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6550 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6550/6550
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 52581..52672: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 24/24 (12 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  843c423 (lane diff = src/c/rgramc.c only,
  +1292/-841; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r14.py, textual C-vs-py
  parse): NEW 14/14 EQ GREEN (S0/S1/AM16/AC72/BM10/
  BC62/M16/QS4/QR4/QT4/QC61 + _N 72/62/61).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Backstop: GATE-12b8957 PASS-functional (sweep) +
  VERIFY-12b8957 PASS (viewer) + PV-12b8957 on file;
  no prior REAUDIT; CLAIM-viewer2-12b8957-r14 oldest
  live reaudit claim (field clear at claim + pre-filing
  re-check, no rival). Q max 361 diff 0.

## verdict: PASS (independent 2nd coverage, concurs GATE+VERIFY)
