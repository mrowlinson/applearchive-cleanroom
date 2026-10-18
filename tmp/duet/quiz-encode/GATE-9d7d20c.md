# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-9d7d20c sweep: RED-tree (same inherited base) / band7 changes PASS

- tip: lanes/encode-cport @9d7d20c (parent f145c51 merge). diff: rgramc.c
  +926/-351 single file (T10PM0..T10PMQ, n<=24484).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-9d7d20c-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 332/332
  IDENTICAL vs py ("332 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 921/921 exact (148 1D + 317 2D + 71 char[] +
  373 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10PMQ correct.
- battery: functional legs all green, outdir gate-cport-9d7d20c-s12:
  C-BUILD w=0, RGRAM n=2988 rc=0, PINS-RGRAM set-eq 2988/2988. no flake.
- parity: RGRAMC-PYID 1494/1494 covered=1494/1494 GREEN rc=0 — FULL.
- C-side RGRAM: 2988/2988 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 24400 PMA, 24415 PMB, 24430/24460/24475 PMQ, 24350 R20.
  (rechecked vs band7 pins: still unpinned.)
- boundaries: 24484 CLOSED-T10PMQ both identical; 24485 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band7 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 196/197 + cport 0/8-held (shared cause).
