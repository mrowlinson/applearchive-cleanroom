# GATE-64b7f1a sweep: PASS-functional (band17; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @64b7f1a. diff: rgramc.c +968/-387 single
  file (T10PS0..T10PSQ, n<=26572).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 368/368
  IDENTICAL vs py ("368 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 991/991 exact (151 1D + 353 2D + 71 char[] +
  404 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PSQ correct.
- battery: functional legs all green, outdir gate-cport-64b7f1a-s12:
  C-BUILD w=0, RGRAM n=3204 rc=0, PINS-RGRAM set-eq 3204/3204. no flake.
- parity: RGRAMC-PYID 1602/1602 covered=1602/1602 GREEN rc=0 — FULL.
- C-side RGRAM: 3204/3204 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 26490 PSA, 26503 PSB, 26520/26550/26565 PSQ, 26470 R26.
  unpinned-ness grepped vs band17 PINS (all FREE).
- boundaries: 26572 CLOSED-T10PSQ both identical; 26573 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 209/210 + cport 18 PASS-functional.
