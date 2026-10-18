# REAUDIT-5db2d64 (viewer4 r10): band131 T10R105 (n<=54320) — PASS

First-hand in fresh WS detached tree
.../reaudit-5db2d64/tree (git archive
5db2d64, full SHA 5db2d6485f1742d0d71
7c7d4efe5a45c6e98d53c), seat-private
build .../build/rgramc (cc -O2 -Wall
-Wextra -std=c11 rc=0 0 warnings,
1622056 bytes). Merged 114f60d.
CLAIM-viewer4-5db2d64-r10 consumed
(claim-check at claim + pre-filing:
no rival).

- PYID (RGRAMC=own r10, corpus 3387
  own-seat hardlinks ex r9 b165 cache,
  all N covered by seed, py+C freshly
  executed per pin): RGRAMC-PYID
  3387/3387 covered=3387/3387,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r10): 6774 PASS
  / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z54320.
- PYBAT (python impl): 6774 PASS / 0
  FAIL, RGRAM-GREEN, rc=0, tail
  g-z54320.
- PINS-RGRAM set-eq 6774/6774 (C/PY
  PASS-name sets cmp-identical, both
  all-PASS).
- Own-loop fresh-oracle 54065..54320:
  pass=256 fail=0 pins=12 pinfail=0,
  OWN-GREEN, rc=0.
- Tables-EQ own script r10 (r9 recipe):
  NEW 2/2 EQ (_T10R105C/_T10R105M);
  FULL 1913/1913 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band
  diff vs ae79d9e (src/c/rgramc.c only,
  +1011/-871, cpat|libcompression|
  depload|dlopen|dylib): 0 hits.
  PINS 6776 lines (6774+2hdr).
  HYGIENE/CONTAM inherit OBSERVED
  (none in lane diff).

VERDICT: PASS (re-confirm; VERIFY
stands; every leg concurs GATE ==
VERIFY). No commits, no push.
