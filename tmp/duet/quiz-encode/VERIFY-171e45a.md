# VERIFY-171e45a cport band221 T10R150 (n<=69980, 914 tiers): PASS

First-hand battery by encode-viewer-r25
in fresh WS NVME .../171e45a-r25/tree
(git archive 171e45a, full SHA
171e45a9a1d8aea0d6f77c9978c3584b7f07b77a),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2117400 bytes == GATE).

- PYID (RGRAMC=own r25, corpus 4486 own-
  seat hardlinks ex r24 b216 + 52 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4538/4538 covered=4538/4538,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r25, fresh oracle):
  9076 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z69980.
- PYBAT (python impl, fresh oracle): 9076
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z69980.
- PINS-RGRAM set-eq 9076/9076 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 69725..69980:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 24/24).
- Tables-EQ own script r25: NEW 4/4 EQ
  (_T10R150C 71x2 + _N=71 derived +
  M16/Q16); FULL 2523/0 (1D 167 + 2D
  901 + STR 302 + STRARR 1153 incl
  11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 3d13ec3 (src/c/rgramc.c only,
  +1328/-1169 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 3d13ec3.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-171e45a on every leg).
Claim note: CLAIM-encode-sweep + CLAIM-
sweep2-96e68e8 gate-prod mentions only;
sole viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
