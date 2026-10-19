# VERIFY-f7d524d cport band224 T10P154 (n<=70420, 920 tiers): PASS

First-hand battery by encode-viewer-r25
in fresh WS NVME .../f7d524d-r25/tree
(git archive f7d524d, full SHA
f7d524d67d7be27f894ee5c5bf2a267b5eafec94),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2134600 bytes == GATE).

- PYID (RGRAMC=own r25, corpus 4678 own-
  seat hardlinks ex r25 b223 + 32 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4582/4582 covered=4582/4582,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r25, fresh oracle):
  9164 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z70420.
- PYBAT (python impl, fresh oracle): 9164
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z70420.
- PINS-RGRAM set-eq 9164/9164 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 70329..70420:
  pass=92 fail=0 pins=32 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 32/32).
- Tables-EQ own script r25: NEW 14/14 EQ
  (T10P154 AC/BC/QC + _N deriveds + M/QR/
  QT/S0/S1/S2); FULL 2548/0 (1D 167 +
  2D 908 + STR 307 + STRARR 1166 incl
  11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 06bd3f5 (src/c/rgramc.c only,
  +1642/-1177 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 06bd3f5.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-f7d524d on every leg).
Claim note: CLAIM-sweep2-f7d524d spent
gate-prod (+ own r25 queue mention-refs);
sole viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
