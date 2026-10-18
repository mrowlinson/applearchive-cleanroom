# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-84c84e1 sweep: RED-tree (same inherited base) / band9 changes PASS

- tip: lanes/encode-cport @84c84e1. diff: rgramc.c +936/-357 single
  file (T10PN0..T10PNQ, n<=24832).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-84c84e1-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 338/338
  IDENTICAL vs py ("338 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 933/933 exact (149 1D + 323 2D + 71 char[] +
  378 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PNQ correct.
- battery: functional legs all green, outdir gate-cport-84c84e1-s12:
  C-BUILD w=0, RGRAM n=3024 rc=0, PINS-RGRAM set-eq 3024/3024. no flake.
- parity: RGRAMC-PYID 1512/1512 covered=1512/1512 GREEN rc=0 — FULL.
- C-side RGRAM: 3024/3024 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 24750 PNA, 24763 PNB, 24780/24800/24820 PNQ, 24720 R21.
  unpinned-ness grepped vs band9 PINS (all FREE).
- boundaries: 24832 CLOSED-T10PNQ both identical; 24833 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band9 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 198/199 + cport 0/10-held (shared cause).
