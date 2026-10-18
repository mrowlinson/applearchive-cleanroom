# VERIFY-df1c35b cport band214 T10P149 (n<=68680, 900 tiers): PASS

First-hand battery by encode-viewer4-r13
in fresh WS detached tree .../r13/verify-
df1c35b/tree (git archive df1c35b, full SHA
df1c35b6bca9fe2775028a9f3034033872ae8255),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
2083240 bytes == GATE).

- PYID (RGRAMC=own r13, corpus 3288 own-
  seat hardlinks ex r12 cbat .rav +
  1154 oracle-regen, py+C freshly
  executed per pin): RGRAMC-PYID
  4442/4442 covered=4442/4442,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r13, fresh oracle):
  8884 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z68680.
- PYBAT (python impl, fresh oracle): 8884
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z68680.
- PINS-RGRAM set-eq 8884/8884 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 68589..68680:
  pass=92 fail=0 pins=16 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE reports
  32/32 = 16x2 closed+sha — same
  16 cells, pinfail=0.)
- Tables-EQ own script r13: NEW 10/10 EQ
  (_T10P149AC/BC/QC/AM/BM/M/QR/QT/S0/S1);
  FULL 2468/2468 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 0fd3076 (src/c/rgramc.c only,
  +1592/-1144 == GATE, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 0fd3076. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (first-hand; agrees with
GATE-df1c35b on every leg).
Claim note: CLAIM-sweep2-df1c35b is spent
gate-prod (r26 handed off 2-cap); sole
viewer claim mine -> unsuffixed.
Quiz diff 0 at file. No commits, no push.
