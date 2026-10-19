# VERIFY-aaed31b cport band226 T10P155 (n<=70768, 924 tiers): PASS

First-hand battery by encode-viewer-r25
in fresh WS NVME .../aaed31b-r25/tree
(git archive aaed31b, full SHA
aaed31b74ec9dc4c501abfbf9b026bdee6566ed1),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2135000 bytes == GATE).

- PYID (RGRAMC=own r25, corpus 4710 own-
  seat hardlinks ex r25 b224 + 32 oracle-
  regen, py+C freshly executed per pin):
  RGRAMC-PYID 4610/4610 covered=4610/4610,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r25, fresh oracle):
  9220 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z70768.
- PYBAT (python impl, fresh oracle): 9220
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z70768.
- PINS-RGRAM set-eq 9220/9220 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 70677..70768:
  pass=92 fail=0 pins=32 pinfail=0,
  OWN-GREEN, rc=0 (=GATE 32/32).
- Tables-EQ own script r25: NEW 14/14 EQ
  (T10P155 AC/BC/QC + _N deriveds + M/QR/
  QT/S0/S1/S2); FULL 2562/0 (1D 167 +
  2D 912 + STR 310 + STRARR 1173 incl
  11 VALS-N).
- Wall-grep PARENT-032 scope on band diff
  vs 33b47ac (src/c/rgramc.c only,
  +1643/-1183 == GATE, cpat|libcompression|
  depload|dlopen|dylib + extended): 0 hits.
  py+PINS+tests cmp-SAME 33b47ac.
  HYGIENE/CONTAM/LIBCOMPRESSION inherit
  OBSERVED (none in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-aaed31b on every leg; GATE's OUTER2
flake is oracle-side, outside VERIFY
scope, documented + proven not tip).
Claim note: CLAIM-sweep2-aaed31b spent
gate-prod (+ own r25 queue mention-refs);
sole viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
