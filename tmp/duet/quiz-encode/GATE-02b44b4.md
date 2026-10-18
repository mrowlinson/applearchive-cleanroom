# GATE-02b44b4 sweep: PASS-functional (band13; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @02b44b4. diff: rgramc.c +512/-374 single
  file (T10R24, n<=25784).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 351/351
  IDENTICAL vs py ("351 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 960/960 exact (151 1D + 336 2D + 71 char[] +
  390 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R24 correct.
- battery: functional legs all green, outdir gate-cport-02b44b4-s12:
  C-BUILD w=0, RGRAM n=3112 rc=0, PINS-RGRAM set-eq 3112/3112. no flake.
- parity: RGRAMC-PYID 1556/1556 covered=1556/1556 GREEN rc=0 — FULL.
- C-side RGRAM: 3112/3112 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 25550/25650/25700/25750/25770 R24, 25520 PPQ.
  unpinned-ness grepped vs band13 PINS (all FREE).
- boundaries: 25784 CLOSED-T10R24 both identical; 25785 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 203/204 + cport 14 PASS-functional.
