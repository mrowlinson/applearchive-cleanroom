# GATE-4ad7a4d sweep: PASS-functional (band16; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @4ad7a4d. diff: rgramc.c +523/-386 single
  file (T10R26, n<=26480).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 363/363
  IDENTICAL vs py ("363 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 982/982 exact (151 1D + 348 2D + 71 char[] +
  400 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R26 correct.
- battery: functional legs all green, outdir gate-cport-4ad7a4d-s12:
  C-BUILD w=0, RGRAM n=3184 rc=0, PINS-RGRAM set-eq 3184/3184. no flake.
- parity: RGRAMC-PYID 1592/1592 covered=1592/1592 GREEN rc=0 — FULL.
- C-side RGRAM: 3184/3184 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 26250/26300/26400/26450/26470 R26, 26215 PRQ.
  unpinned-ness grepped vs band16 PINS (all FREE).
- boundaries: 26480 CLOSED-T10R26 both identical; 26481 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 207/208 + cport 17 PASS-functional.
