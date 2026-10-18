# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-a0adca4 sweep: RED-tree (same inherited base) / band11 changes PASS

- tip: lanes/encode-cport @a0adca4. diff: rgramc.c +940/-363 single
  file (T10PO0..T10POQ, n<=25180).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-a0adca4-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical): top-level dispatch bounds 344/344
  IDENTICAL vs py ("344 tiers sealed" exact); CLOSED tag sets
  IDENTICAL; tables 944/944 exact (149 1D + 329 2D + 71 char[] +
  383 char*[] + 11 dicts + local _s re-verified unchanged);
  top label T10POQ correct.
- battery: functional legs all green, outdir gate-cport-a0adca4-s12:
  C-BUILD w=0, RGRAM n=3060 rc=0, PINS-RGRAM set-eq 3060/3060. no flake.
- parity: RGRAMC-PYID 1530/1530 covered=1530/1530 GREEN rc=0 — FULL.
- C-side RGRAM: 3060/3060 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 25095 POA, 25110 POB, 25130/25160/25175 POQ, 25080 R22.
  unpinned-ness grepped vs band11 PINS (all FREE).
- boundaries: 25180 CLOSED-T10POQ both identical; 25181 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band11 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 201/202 + cport 0/12-held (shared cause).
