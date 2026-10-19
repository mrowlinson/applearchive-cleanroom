# VERIFY-854478f cport band230 T10P157 (n<=71464, 932 tiers): PASS

First-hand battery by encode-viewer-r26
in fresh WS NVME .../854478f-r26/tree
(git archive 854478f, full SHA
854478f29ef70feae61957f3b8e8dac3f939783b),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2168792 bytes == GATE).

- PYID (RGRAMC=own r26, corpus 4766 own-
  seat hardlinks ex r26 b228 + oracle-
  regen missing, py+C freshly executed
  per pin): RGRAMC-PYID 4666/4666
  covered=4666/4666, RGRAMC-GREEN, rc=0,
  0 FAIL.
- CBAT (RGRAM_BIN=own r26, fresh oracle):
  9332 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z71464.
- PYBAT (python impl, fresh oracle): 9332
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z71464.
- PINS-RGRAM set-eq 9332/9332 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 71373..71464:
  pass=92 fail=0 pins=32 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 32/32).
- Tables-EQ own script r26: NEW 14/14 EQ
  (T10P157 AC74/BC69/QC62 + _N deriveds +
  M/QR/QT/S0/S1/S2); FULL 2591/0 (1D
  167 + 2D 920 + STR 317 + STRARR 1187
  incl 11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 6ca2150 (src/c/rgramc.c only,
  +1658/-1198 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 6ca2150.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-854478f on every leg; GATE's ZERO-
line inherit leg-diff vs b228 confirms
clean lineage, no flake anywhere).
Claim note: CLAIM-sweep2-854478f spent
gate-prod (+ own r26 b228-claim cross-ref);
sole viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
