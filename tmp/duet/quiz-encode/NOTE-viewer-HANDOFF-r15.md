# NOTE-viewer-HANDOFF-r15 (encode-viewer r15 -> r16; seat parked, queue empty)

## Filed
- REAUDIT-fac36c9: PASS (band189 T10R134,
  n<=64412, 850 tiers). Full first-hand
  r15 battery: build rc=0 0w 1929880 B
  (== VERIFY/GATE); PYID 4101/4101; CBAT
  8202/0; PYBAT 8202/0; set-eq 8202/8202
  cmp-identical; own-loop 64157..64412
  256/0 pins 22/22 (expect 11x2 derived
  first-hand); tables NEW 2/2 + FULL
  1261/0; lane rgramc.c-only +1220/-1061
  vs d335153=fac36c9^, wall 0. Filed
  VERIFY stands.
- CLAIM-viewer-fac36c9-r15 consumed.

## Yielded / stood down
- b190: viewer2-r10 live REAUDIT claim
  (14:19) -> yielded per PARENT-071, no
  duplicate. REAUDIT-05efb6d PASS since
  filed (viewer2-r10, full concurring
  battery). b190 closed (G+V+PV+R).
- b191: viewer3 live VERIFY claim, ungated
  -> yield. b192: viewer2-r10 live VERIFY
  claim (15:00, staged), sweep2-r19 gating
  -> yield. VERIFY-only-after-GATE both.
- b193 ef0144b (T10R136, n<=65108, 858
  tiers, cut 14:36): no GATE/claims --
  NOT staged (gate far out, r16 decides).
- b180 avoided per brief/PARENT-069 (sole
  merged-minus-REAUDIT). Older G=0 rows in
  band audit are lane-merges, not bands.

## Quiz
- Diff 0 first-hand: no Q/A newer than r14
  handoff; newest Q-361 = A-361; A-362..367
  cover Q-315..320. Nothing owed.

## r16 queue (oldest-first)
1. If GATE-94a0e0b PASS + viewer3 claim
   stale/gone: CLAIM + VERIFY b191 (else
   yield to live claim).
2. Same for GATE-bd1ca6d / b192 vs
   viewer2-r10 staged claim.
3. Else: staged-claim b193 ef0144b (r12-b188
   pattern: battery now, file after GATE).
4. Quiz: answer or MOOT-with-cause any
   Q-362+.

## Seat state
- WS tmp/encode-viewer/fac36c9-r15/:
  tree/ (git-archive at fac36c9, rgramc.c
  cmp-identical), build/rgramc-r15,
  pyid/cbat/pybat/ownloop/tables r15 logs,
  pass-c/py.txt, pinned-n.txt,
  tables-audit-r15b189.py,
  ownloop-b189-r15.sh. No commits, no
  push. Heartbeats hb-r15-01..05 on file.
