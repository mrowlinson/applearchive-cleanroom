# GATE-ff3ef8a sweep: PASS-functional (band14; inherited legs OBSERVED per 032)

- tip: lanes/encode-cport @ff3ef8a. diff: rgramc.c +954/-375 single
  file (T10PQ0..T10PQQ, n<=25876).
- tree legs: HYGIENE/CONTAM/LIBCOMPRESSION trip on the ruled
  inherited base — OBSERVED-inherited per PARENT-032, never lane
  FAIL. no FLAG filed (033 stop-refiling). lane-diff wall grep
  CLEAN (0 hits).
- code read (FULL-mechanical): top-level dispatch bounds 356/356
  IDENTICAL vs py ("356 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 969/969 exact (151 1D + 341 2D + 71 char[] +
  394 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PQQ correct.
- battery: functional legs all green, outdir gate-cport-ff3ef8a-s12:
  C-BUILD w=0, RGRAM n=3132 rc=0, PINS-RGRAM set-eq 3132/3132. no flake.
- parity: RGRAMC-PYID 1566/1566 covered=1566/1566 GREEN rc=0 — FULL.
- C-side RGRAM: 3132/3132 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 25795 PQA, 25808 PQB, 25825/25850/25870 PQQ, 25770 R24.
  unpinned-ness grepped vs band14 PINS (all FREE).
- boundaries: 25876 CLOSED-T10PQQ both identical; 25877 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- verdict: PASS-functional; mergeable per 032.
  coverage: w2 205/206 + cport 15 PASS-functional.
