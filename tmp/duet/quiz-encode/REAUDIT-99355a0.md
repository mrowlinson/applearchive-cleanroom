# REAUDIT-99355a0: band115 T10P99 (n<=51280, 700 tiers) — PASS

First-hand re-battery by encode-viewer4-r13
in fresh WS detached tree .../r13/reaudit-
99355a0/tree (git archive 99355a0, full SHA
99355a0b4f0965e9262895f68e5467b1cff19d9f),
seat-private build .../build/rgramc (cc -O2
-Wall -Wextra -std=c11 rc=0 0 warnings,
1553192 bytes).

- PYID (RGRAMC=own r13, corpus 3288 own-
  seat hardlinks ex r12 cbat .rav cache,
  py+C freshly executed per pin):
  RGRAMC-PYID 3171/3171 covered=3171/3171,
  RGRAMC-GREEN, rc=0, 0 FAIL.
- CBAT (RGRAM_BIN=own r13, fresh oracle):
  6342 PASS / 0 FAIL, RGRAM-GREEN, rc=0,
  tail g-z51280.
- PYBAT (python impl, fresh oracle): 6342
  PASS / 0 FAIL, RGRAM-GREEN, rc=0, tail
  g-z51280.
- PINS-RGRAM set-eq 6342/6342 (C/PY PASS-
  name sets cmp-identical, both all-PASS).
- Own-loop fresh-oracle 51189..51280:
  pass=92 fail=0 pins=15 pinfail=0,
  OWN-GREEN, rc=0. (Pin convention:
  closed-rows in range; GATE/VERIFY
  report 30/30 = 15x2 closed+sha — same
  15 cells, pinfail=0.)
- Tables-EQ own script r13: NEW 10/10 EQ
  (_T10P99AC/BC/QC/AM/BM/M/QR/QT/S0/S1);
  FULL 1811/1811 0-skip 0-mismatch.
- Wall-grep PARENT-032 scope on band diff
  vs 2058487 (src/c/rgramc.c only,
  +1254/-817 == GATE, cpat|libcompression|
  depload|dlopen|dylib): 0 hits. py+PINS+
  tests cmp-SAME 2058487. HYGIENE/CONTAM/
  LIBCOMPRESSION inherit OBSERVED (none
  in lane diff).

VERDICT: PASS (re-confirm; VERIFY stands;
agrees with GATE/VERIFY on every leg).
Quiz diff 0 at file. No commits, no push.
