# GATE-6b87eaf sweep: PASS-functional (band21; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @6b87eaf. diff: rgramc.c +986/-405 single
  file (T10PV0..T10PVQ, n<=27616).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 386/386
  IDENTICAL vs py ("386 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 1025/1025 exact (152 1D + 371 2D + 71 char[] +
  419 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PVQ correct.
- battery: functional legs all green, outdir gate-cport-6b87eaf-s12:
  C-BUILD w=0, RGRAM n=3312 rc=0, PINS-RGRAM set-eq 3312/3312. no flake.
- parity: RGRAMC-PYID 1656/1656 covered=1656/1656 GREEN rc=0 — FULL.
- C-side RGRAM: 3312/3312 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 27535 PVA, 27548 PVB, 27565/27600/27610 PVQ, 27522 R29.
  unpinned-ness grepped vs band21 PINS (all FREE).
- boundaries: 27616 CLOSED-T10PVQ both identical; 27617 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 214/215 + cport 22 PASS-functional.
