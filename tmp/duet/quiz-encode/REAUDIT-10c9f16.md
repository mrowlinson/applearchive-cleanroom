# REAUDIT-10c9f16 (viewer4 r10): band159 T10R119 (n<=59192) — PASS

First-hand in fresh WS detached tree
.../reaudit-10c9f16/tree (git archive
10c9f16, full SHA 10c9f16f46672404775
94746a50a41bd0862e725), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1775800 bytes). Merged 32d59e5.
CLAIM-viewer4-10c9f16-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3732
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3732/3732 covered=3732/3732,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7464 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z59192.
- PYBAT (python impl): 7464 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z59192.
- PINS-RGRAM set-eq 7464/7464 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 58937..59192:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  26/26 = 13x2 closed+sha — same 13
  cells, pinfail=0.)
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R119C/_T10R119M);
  FULL 2095/2095 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 5b5ae12 (src/c/rgramc.c only,
  +1104/-963, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7466 lines (7464+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
