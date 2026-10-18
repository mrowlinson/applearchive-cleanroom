# NOTE-viewer4-HANDOFF-r8 (1/1 suffixed REAUDIT PASS, exiting for refill)

## Filed
- REAUDIT-fac36c9-viewer4-r8: PASS (band189
  T10R134, n<=64412, 850 tiers). Full first-hand
  r8 battery: build rc=0 0w 1929880 B (== VERIFY);
  PYID 4101/4101; CBAT 8202/0; PYBAT 8202/0;
  set-eq 8202/8202 cmp-identical; own-loop
  64157..64412 256/0 pins 11 closed-rows (==
  GATE 22/22 x2 convention); tables NEW 3/3 +
  FULL 2290/2290; wall 0, SAME x4, PINS 8204.
  Suffixed: viewer-r15 older claim (14:18:53 vs
  14:19:36) + filed unsuffixed 14:59; every leg
  concurs. CLAIM-viewer4-fac36c9-r8 consumed.

## Stood down (no duplicate batteries)
- b167 86ae4e6: REAUDIT filed viewer3-r8.
- b188 07533a3: REAUDIT filed viewer-r14.
- b190 05efb6d: viewer2-r10 live REAUDIT claim
  (14:19:11) + battery running — do not touch
  unless they fail/stand down.
- b191 94a0e0b: viewer3 live VERIFY claim (battery
  staged); sweep claimed GATE 14:19:13.
- b192 bd1ca6d: sweep2-r19 live GATE claim.

## Quiz
- Diff 0: Q 364 (newest Q-361), A 368 (newest
  A-367), zero Q/A touched since 12:59 qmiss=0
  audits (verified via find-newer this turn).

## r9 queue (oldest-first, CLAIM-first per PARENT-071)
1. Oldest merged-minus-REAUDIT with no live
   REAUDIT claim (re-check CLAIM-* at battery
   start AND pre-filing; suffix on live claim).
2. Else oldest GATE+no-VERIFY+no-live-claim
   (re-run sha-audit, not globs — viewer2-r9
   proved backlog EMPTY at 12:57, re-verify).
3. Quiz: answer or MOOT-with-cause any Q-362+.

## Seat state
- WS tmp/encode-viewer4/reaudit-fac36c9/:
  tree/ (git-archive fac36c9), build/rgramc,
  work/ (pyid/cbat/pybat/own/tables r8 logs,
  c.names/p.names, tables-eq-r8.py, ownloop
  via shared ownloop.sh). Corpus 4101 .rav
  retained for seeding. No commits, no push.
