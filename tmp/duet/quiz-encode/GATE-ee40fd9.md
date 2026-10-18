# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-ee40fd9 sweep: RED-tree (same inherited base) / Makefile PASS

- tip: lanes/encode-cport @ee40fd9 (parent e64e2da held). diff:
  src/c/Makefile +6/-0 ONLY (.PHONY aae/rgramc aliases).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-ee40fd9-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL, 6 lines): phony short names route bare
  `make rgramc`/`make aae` to $(BUILDDIR) targets instead of the
  implicit rule. `all` untouched. correct minimal fix.
- behavior verified first-hand (NVME extracts): tip `make rgramc
  BUILDDIR=...` rc=0, binary in builddir, ZERO srcdir droppings,
  0 warnings. parent same command DROPS ./rgramc in srcdir —
  bug confirmed, fix confirmed.
- battery: functional legs all green, outdir gate-cport-ee40fd9-s12:
  C-BUILD w=0, RGRAM n=2968 rc=0, PINS-RGRAM set-eq 2968/2968. no flake.
- parity: rgramc.c byte-identical to gated band6 (diff 0 bytes) —
  1484/1484 FULL evidence carries; 3-cell spot on tip binary SAME
  (100 T0, 24045 PL0, 24392 R20). storm/boundaries carried likewise.
- wall: diff grep CLEAN (1 hunk-header FP only).
- verdict: Makefile changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 195/196 + cport 0/7-held (shared cause).
