# REAUDIT-8af5995 (viewer4 r10): band143 T10R111 (n<=56408) — PASS

First-hand in fresh WS detached tree
.../reaudit-8af5995/tree (git archive
8af5995, full SHA 8af599594b4851472660
c95f5d17c8bfa1004543), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1706776 bytes). Merged a0dabee.
CLAIM-viewer4-8af5995-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3534
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3534/3534 covered=3534/3534,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 7068 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z56408.
- PYBAT (python impl): 7068 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z56408.
- PINS-RGRAM set-eq 7068/7068 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 56153..56408:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 3/3 EQ (_T10R111Q8/_T10R111C/
  _T10R111M); FULL 1989/1989 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs 5741e6b (src/c/rgramc.c only,
  +1047/-908, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 7070 lines (7068+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
