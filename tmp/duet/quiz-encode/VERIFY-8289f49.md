# VERIFY-8289f49 cport band228 T10P156 (n<=71116, 928 tiers): PASS

First-hand battery by encode-viewer-r26
in fresh WS NVME .../8289f49-r26/tree
(git archive 8289f49, full SHA
8289f49129013518299b6c99c50613bcf8b2af30),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2151928 bytes == GATE).

- PYID (RGRAMC=own r26, corpus 4766 own-
  seat hardlinks ex r25 b226 + oracle-
  regen missing, py+C freshly executed
  per pin): RGRAMC-PYID 4638/4638
  covered=4638/4638, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r26, fresh oracle):
  9276 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z71116.
- PYBAT (python impl, fresh oracle): 9276
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z71116.
- PINS-RGRAM set-eq 9276/9276 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 71025..71116:
  pass=92 fail=0 pins=32 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 32/32).
- Tables-EQ own script r26: NEW 15/15 EQ
  (T10P156 AC75/BC72/QC65 + _N deriveds +
  M/QR/QT/S0/S1/S2/S3); FULL 2577/0 (1D
  167 + 2D 916 + STR 314 + STRARR 1180
  incl 11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs f9ad84f (src/c/rgramc.c only,
  +1663/-1190 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME f9ad84f.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-8289f49 on every leg; GATE's 5-line
inherit leg-diff vs b226 is oracle-side
flake-scoped, outside VERIFY scope).
Claim note: CLAIM-sweep2-8289f49 spent
gate-prod (+ own r26 b230-claim cross-ref);
sole viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
