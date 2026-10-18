# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-e64e2da sweep: RED-tree (same inherited base) / band6 changes PASS

- tip: lanes/encode-cport @e64e2da (parent 2dbd144 merge). diff: rgramc.c
  +1074/-345 single file (T10PL0..T10R20, n<=24392).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-e64e2da-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 327/327
  IDENTICAL vs py ("327 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 912/912 exact (148 1D + 312 2D + 71 char[] +
  369 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10R20 correct.
- battery: functional legs all green, outdir gate-cport-e64e2da-s12:
  C-BUILD w=0, RGRAM n=2968 rc=0, PINS-RGRAM set-eq 2968/2968. no flake.
- parity: RGRAMC-PYID 1484/1484 covered=1484/1484 GREEN rc=0 — FULL.
- C-side RGRAM: 2968/2968 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 24050 PLA, 24100 PLQ, 24200/24250/24300/24350 R20.
- boundaries: 24392 CLOSED-T10R20 both identical; 24393 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band6 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 195/196 + cport 0/6-held (shared cause).
