# GATE-696bb26 sweep: PASS-functional (band20; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @696bb26. diff: rgramc.c +1120/-399 single
  file (T10PU0..T10PUQ+T10R29, n<=27524).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 381/381
  IDENTICAL vs py ("381 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 1016/1016 exact (152 1D + 366 2D + 71 char[] +
  415 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R29 correct.
- battery: functional legs all green, outdir gate-cport-696bb26-s12:
  C-BUILD w=0, RGRAM n=3292 rc=0, PINS-RGRAM set-eq 3292/3292. no flake.
- parity: RGRAMC-PYID 1646/1646 covered=1646/1646 GREEN rc=0 — FULL.
- C-side RGRAM: 3292/3292 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 27185 PUA, 27200 PUB, 27300/27400/27500/27522 R29.
  unpinned-ness grepped vs band20 PINS (all FREE).
- boundaries: 27524 CLOSED-T10R29 both identical; 27525 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 213/214 + cport 21 PASS-functional.
