# NOTE-viewer4-HANDOFF-r9 (1/1 suffixed REAUDIT PASS, exiting for refill)

## Filed
- REAUDIT-7f4db2c-viewer4-r9: PASS
  (band165 T10R122, n<=60236, 802
  tiers). Full first-hand r9 battery:
  build rc=0 0w 1809880 B (== VERIFY);
  PYID 3807/3807; CBAT 7614/0; PYBAT
  7614/0; set-eq 7614/7614
  cmp-identical; own-loop 59981..60236
  256/0 pins 12 (== VERIFY 24/24 x2
  convention); tables NEW 2/2 + FULL
  2133/2133; wall 0, SAME parent
  399f71d, PINS 7616. Suffixed:
  viewer-r17 older claim (17:12:03 vs
  17:12:24) + filed unsuffixed; every
  leg concurs. CLAIM-viewer4-7f4db2c-r9
  consumed. (First PYID RED was seat
  method error — RGRAMC unset, ancient
  shared binary; hb-r9-04. Only the
  own-binary GREEN run cited.)

## Stood down (no duplicate batteries)
- b195 3744141: GATE+VERIFY closed
  (viewer2-r10/sweep-r15).
- b196 4c9ff15: GATE filed (sweep2-r19);
  viewer3-r10 live staged VERIFY claim.
- b197 f11a1ca: viewer2-r10 VERIFY +
  sweep GATE claims live. b198 6bf6af5:
  sweep2 GATE claim live.
- b163 e1a5f7c: viewer-r18 live REAUDIT
  claim (window extending below b164).

## Quiz
- Diff 0: Q 364 (newest Q-361), A 368,
  zero Q/A touched all run (rechecked
  pre-filing).

## r10 queue (oldest-first, CLAIM-first per PARENT-071)
1. REAUDIT backfill below b164 (r18
   precedent: b163 taken): oldest
   0-REAUDIT merged cport band with no
   live REAUDIT claim (b164+ window now
   fully covered except avoided b180;
   re-check CLAIM-* at battery start AND
   pre-filing; suffix on live claim).
   Caution: older commits may carry an
   older harness — confirm battery
   scripts at-commit before claiming.
2. Else oldest GATE+no-VERIFY+no-live-
   claim in cport band flow (13 ancient
   R86-P93 individual gates excluded by
   convention — archaeology, owner call).
3. Quiz: answer or MOOT-with-cause any
   Q-362+.

## Seat state
- WS tmp/encode-viewer4/reaudit-7f4db2c/:
  tree/ (git-archive 7f4db2c), build/
  rgramc, work/ (pyid/cbat/pybat/own/
  tables r9 logs, c.names/p.names,
  tables-eq-r9.py, ownloop via shared
  ownloop.sh). Corpus 4101 .rav
  retained for seeding. No commits, no
  push.
