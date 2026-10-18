# GATE-55494eb sweep: PASS-functional (band15; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @55494eb. diff: rgramc.c +1094/-380 single
  file (T10R25+T10PR0..T10PRQ, n<=26224).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 362/362
  IDENTICAL vs py ("362 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 980/980 exact (151 1D + 347 2D + 71 char[] +
  399 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PRQ correct.
- battery: functional legs all green, outdir gate-cport-55494eb-s12:
  C-BUILD w=0, RGRAM n=3168 rc=0, PINS-RGRAM set-eq 3168/3168. no flake.
- parity: RGRAMC-PYID 1584/1584 covered=1584/1584 GREEN rc=0 — FULL.
- C-side RGRAM: 3168/3168 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 25900 R25, 26140 PRA, 26155 PRB, 26175/26200/26215 PRQ.
  unpinned-ness grepped vs band15 PINS (all FREE).
- boundaries: 26224 CLOSED-T10PRQ both identical; 26225 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 206/207 + cport 16 PASS-functional.
