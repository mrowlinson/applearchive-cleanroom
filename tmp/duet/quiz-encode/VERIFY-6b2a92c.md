# VERIFY-6b2a92c cport band215 T10R147 (n<=68936, 902 tiers): PASS

First-hand battery by encode-viewer-r24
in fresh WS NVME .../6b2a92c-r24/tree
(git archive 6b2a92c, full SHA
6b2a92c92149411f16a6eb013bcbf294c53a4180),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2083288 bytes).

- PYID (RGRAMC=own r24, corpus 4426 own-
  seat hardlinks ex r24 b213 + 56 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4454/4454 covered=4454/4454,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r24, fresh oracle):
  8908 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z68936.
- PYBAT (python impl, fresh oracle): 8908
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z68936.
- PINS-RGRAM set-eq 8908/8908 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 68681..68936:
  pass=256 fail=0 pins=24 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 24/24, 12x2
  closed+sha).
- Tables-EQ own script r24: NEW 4/4 EQ
  (_T10R147C + _N derived + M + Q);
  FULL 2482/0 (1D 167 + 2D 889 + STR
  294 + STRARR 1132 incl 11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 8bed83b (src/c/rgramc.c only,
  +1308/-1149 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 8bed83b.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-6b2a92c on every leg).
Claim note: CLAIM-sweep-6b2a92c spent
gate-prod (r16g moved on); sole viewer
claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
