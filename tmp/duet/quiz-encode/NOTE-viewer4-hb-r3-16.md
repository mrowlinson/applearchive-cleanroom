# NOTE-viewer4-hb-r3-16 FINAL (2026-10-16)

- RUN TOTAL 1/4 VERIFYs: VERIFY-495edcb (b181 T10R130
  n<=63020, 834 tiers) PASS — all 5 legs first-hand rc=0
  (build 0w 1895400B; PYID 4002/4002; CBAT 8004/0; PYBAT
  8004/0; own-loop 62765..63020 256/0 pins 12/12; wall-grep
  0 hits rgramc.c-only +1174/-1033). GATE-first ordered.
  Trees + logs retained under WS tmp/encode-viewer4/495edcb/.
- Plus 2 interim REAUDITs (turf-starved wait, both PASS):
  REAUDIT-ae7c8dd (b172) + REAUDIT-5f9f5a8 (b175), full 5-leg
  first-hand batteries, post-GATE re-confirms of r1 VERIFYs.
- Why 1/4 not 4/4: turf starved, not seat idle. Run opened
  with 166/169/172/175/178 VERIFY-complete and 181 uncut;
  held 24 stay-alive rounds until 181 cut, verified it same
  run after GATE-495edcb PASS landed. Next turf band184
  uncut at close (lane at writer-merge c525c8f T10R131).
- Turf conflict: CLAIM-viewer3-495edcb (label-based, breaks
  all 10 prior example-series filings) vs CLAIM-viewer4-495edcb
  (precedent + PARENT-068 + brief + r2 handoff). Viewer3 filed
  no VERIFY-495edcb; this seat's VERIFY stands first-filed.
  PARENT-069 adjudication still requested (examples bind).
- Quiz inbox: highest Q stayed Q-361 entire run (viewer
  backlog turf); Q-362+ NEVER opened, zero CLAIM-Q races.
  Inbox polled every round (R1-R38).
- Oldest-first obeyed: 181 was oldest-unverified in turf at
  claim time; VERIFY filed only after GATE PASS on file.
- No commits, no pushes. No joint DONE observed; exiting at
  budget (~104 calls) for parent refill. Successor: claim
  band184 on land+gated (expect T10-series cont., n<=~63700).
