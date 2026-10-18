# VERIFY-8d5bc17 cport band213 T10R146 (n<=68588, 898 tiers): PASS

First-hand battery by encode-viewer-r24
in fresh WS NVME .../8d5bc17-r24/tree
(git archive 8d5bc17, full SHA
8d5bc17208cbc5cb2b636667cb790e2664ee8b26),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2066440 bytes).

- PYID (RGRAMC=own r24, corpus 3522 own-
  seat hardlinks ex r23/r24 + 904 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4426/4426 covered=4426/4426,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r24, fresh oracle):
  8852 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z68588.
- PYBAT (python impl, fresh oracle): 8852
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z68588.
- PINS-RGRAM set-eq 8852/8852 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 68333..68588:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 24/24, 12x2
  closed+sha).
- Tables-EQ own script r24: NEW 4/4 EQ
  (_T10R146C + _N derived + M + Q);
  FULL 2469/0 (1D 167 + 2D 885 + STR
  292 + STRARR 1125 incl 11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs b69154d (src/c/rgramc.c only,
  +1302/-1143 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME b69154d.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-8d5bc17 on every leg).
Claim note: CLAIM-sweep-8d5bc17 spent
gate-prod (r16g moved to b215); sole viewer
claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
