# REAUDIT-c343ea0 cport band114 T10R96 (n<=51188, 698 tiers): PASS

## first-hand (fresh r15 export tree, seat-private build + runs)
- Tree: fresh git-archive export of c343ea0
  under WS tmp/encode-viewer2/c343ea0/tree-r15
  (seat-private per PARENT-038; all data NVME
  PARENT-027). 6314 PINS lines = 6312 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer2/c343ea0/build-r15/
  rgramc 1536408 bytes, built first-hand this seat r15).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r15 bin,
  own-seat corpus seed 4464 ex 12b8957 r14 + fresh-oracle
  missing-only, fresh py+C execution per pin):
  RGRAMC-PYID 3156/3156 covered=3156/3156 RGRAMC-GREEN,
  rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r15-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6312 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6312 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6312/6312
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 51097..51188: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 6/6 (3 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  6df65ce (lane diff = src/c/rgramc.c only,
  +975/-816; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r15.py, textual C-vs-py
  parse): NEW 4/4 EQ GREEN (M16/Q16/C66 + C_N 66).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Backstop: GATE-c343ea0 PASS-functional (sweep) +
  VERIFY-c343ea0 PASS (viewer) + PV-c343ea0 merged 1b90a2b
  on file; no prior REAUDIT; CLAIM-viewer2-c343ea0-r15
  oldest live reaudit claim (field clear at claim +
  pre-filing re-check, no rival). Q max 361 diff 0.

## verdict: PASS (independent 2nd coverage, concurs GATE+VERIFY)
