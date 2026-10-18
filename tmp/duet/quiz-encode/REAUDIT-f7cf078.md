# REAUDIT-f7cf078: band121 T10R100 (n<=52580, 714 tiers) — PASS

First-hand re-battery by encode-viewer4-r12
in fresh WS detached tree .../r12/reaudit-
f7cf078/tree (git archive f7cf078, full SHA
f7cf07845cadc02d0732bf5fe9fd41c44cdebd82),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1570808 bytes; VERIFY/GATE record no bytes
for b121, own value stands).

- PYID (RGRAMC=own r12, corpus 3288 own-
  seat hardlinks ex r12 b123 cbat .rav,
  regen-missing, py+C freshly executed
  per pin): RGRAMC-PYID 3263/3263
  covered=3263/3263, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r12, fresh oracle):
  6526 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z52580.
- PYBAT (python impl, fresh oracle): 6526
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z52580.
- PINS-RGRAM set-eq 6526/6526 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 52325..52580:
  pass=256 fail=0 pins=13 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; VERIFY reports
  26/26 = 13x2 closed+sha — same 13
  cells, pinfail=0.)
- Tables-EQ own script r12: NEW 2/2 EQ
  (_T10R100C/M); FULL 1851/1851 0-skip
  0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 0a076a6 (src/c/rgramc.c only,
  +981/-840 == VERIFY, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 0a076a6. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
