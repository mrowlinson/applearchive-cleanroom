# GATE-a55b78c sweep: PASS-functional (band19; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @a55b78c. diff: rgramc.c +535/-398 single
  file (T10R28, n<=27176).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 375/375
  IDENTICAL vs py ("375 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 1004/1004 exact (151 1D + 360 2D + 71 char[] +
  410 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R28 correct.
- battery: functional legs all green, outdir gate-cport-a55b78c-s12:
  C-BUILD w=0, RGRAM n=3256 rc=0, PINS-RGRAM set-eq 3256/3256. no flake.
- parity: RGRAMC-PYID 1628/1628 covered=1628/1628 GREEN rc=0 — FULL.
- C-side RGRAM: 3256/3256 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 26950/27050/27100/27150/27170 R28, 26915 PTQ.
  unpinned-ness grepped vs band19 PINS (all FREE).
- boundaries: 27176 CLOSED-T10R28 both identical; 27177 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 211/212 + cport 20 PASS-functional.
