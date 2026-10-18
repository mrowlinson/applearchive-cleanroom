# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-b6a42aa sweep: RED-tree (same inherited base) / band8 changes PASS

- tip: lanes/encode-cport @b6a42aa (parent 10eb4bb merge). diff: rgramc.c
  +494/-356 single file (T10R21, n<=24740).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-b6a42aa-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 333/333
  IDENTICAL vs py ("333 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 924/924 exact (149 1D + 318 2D + 71 char[] +
  374 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R21 correct.
- battery: functional legs all green, outdir gate-cport-b6a42aa-s12:
  C-BUILD w=0, RGRAM n=3004 rc=0, PINS-RGRAM set-eq 3004/3004. no flake.
- parity: RGRAMC-PYID 1502/1502 covered=1502/1502 GREEN rc=0 — FULL.
- C-side RGRAM: 3004/3004 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 24500/24600/24650/24700/24720 R21, 24475 PMQ.
  unpinned-ness grepped vs band8 PINS (all FREE).
- boundaries: 24740 CLOSED-T10R21 both identical; 24741 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band8 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 197/198 + cport 0/9-held (shared cause).
