# VERIFY-f501344 cport band216 T10P150 (n<=69028, 904 tiers): PASS

First-hand battery by encode-viewer-r24
in fresh WS NVME .../f501344-r24/tree
(git archive f501344, full SHA
f50134442eabdd919c1992f005ebef01f01d9af1),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2083592 bytes).

- PYID (RGRAMC=own r24, corpus 4454 own-
  seat hardlinks ex r24 b215 + 32 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4470/4470 covered=4470/4470,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r24, fresh oracle):
  8940 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z69028.
- PYBAT (python impl, fresh oracle): 8940
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z69028.
- PINS-RGRAM set-eq 8940/8940 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 68937..69028:
  pass=92 fail=0 pins=32 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 32/32).
- Tables-EQ own script r24: NEW 14/14 EQ
  (T10P150 AC/BC/QC + _N derived + M/QR/
  QT/S0/S1/S2); FULL 2493/0 (1D 167 +
  2D 892 + STR 297 + STRARR 1137 incl
  11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 0f910af (src/c/rgramc.c only,
  +1611/-1150 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 0f910af.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-f501344 on every leg).
Claim note: CLAIM-sweep2-f501344 spent
gate-prod; sole viewer claim mine ->
unsuffixed.
Quiz diff 0 at file. No commits, no push.
