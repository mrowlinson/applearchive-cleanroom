# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-a99d06a sweep: RED-tree (same inherited base) / band10 changes PASS

- tip: lanes/encode-cport @a99d06a. diff: rgramc.c +499/-362 single
  file (T10R22, n<=25088).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-a99d06a-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 339/339
  IDENTICAL vs py ("339 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 935/935 exact (149 1D + 324 2D + 71 char[] +
  379 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R22 correct.
- battery: functional legs all green, outdir gate-cport-a99d06a-s12:
  C-BUILD w=0, RGRAM n=3040 rc=0, PINS-RGRAM set-eq 3040/3040. no flake.
- parity: RGRAMC-PYID 1520/1520 covered=1520/1520 GREEN rc=0 — FULL.
- C-side RGRAM: 3040/3040 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 24850/24900/25000/25050/25080 R22, 24820 PNQ.
  unpinned-ness grepped vs band10 PINS (all FREE).
- boundaries: 25088 CLOSED-T10R22 both identical; 25089 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band10 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 199/200 + cport 0/11-held (shared cause).
