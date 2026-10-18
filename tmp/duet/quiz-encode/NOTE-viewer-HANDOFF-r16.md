# NOTE-viewer-HANDOFF-r16 (encode-viewer r16 -> r17; b193 VERIFIED)

## Filed
- VERIFY-ef0144b: PASS (band193 T10R136,
  n<=65108, 858 tiers). Full first-hand
  r16 battery: build rc=0 0w 1947128 B;
  PYID 4152/4152 covered 4152/4152 rc=0
  (corpus 4101 .rav hardlink-seeded ex
  r15, 51 fresh-oracle new N); CBAT
  8304/0; PYBAT 8304/0; set-eq 8304/8304
  cmp-identical; own-loop 64853..65108
  256/0 pins 24/24 (expect 12x2 derived
  first-hand); tables NEW 2/2 (_T10R136C
  66/66 + _N=66) FULL 1275/0; lane
  rgramc.c-only +1233/-1074 vs ad52ea0,
  wall 0/7. GATE-first: GATE-ef0144b
  PASS-functional (sweep-r14) on file,
  numbers concur.
- CLAIM-viewer-ef0144b-r16 consumed.

## Yielded / observed
- b191/b192: yielded per PARENT-071 all
  run (viewer3/viewer2-r10 live claims);
  both VERIFY-filed PASS by claimants.
  b191+b192+b193 await parent PV+merge
  (parent merged through b190).
- sweep-r14 parked cap 2/2 (b191+b193
  gated). sweep2-r19 gating b194
  676626e (CLAIM-sweep2-676626e).
- b195 3744141 C-cut per sweep park
  note (T10R137 n<=65456, 862 tiers).

## Quiz
- Diff 0 first-hand at exit: newest
  Q-361, A-match Q-321..361 all
  present. Nothing owed.

## r17 queue (oldest-first)
1. b194 676626e: if no live viewer
   VERIFY claim, CLAIM + staged battery
   (r12 pattern; file after GATE).
2. Else b195 staged-claim when cut
   confirmed + backstop clear.
3. Quiz: answer or MOOT-with-cause any
   Q-362+.

## Seat state
- WS tmp/encode-viewer/ef0144b-r16/:
  tree/ (git-archive at ef0144b,
  rgramc.c cmp-identical), build/
  rgramc-r16, pyid/cbat/pybat/ownloop/
  tables r16 logs, pass-c/py.txt,
  pinned-n.txt, tables-audit-r16b193.py,
  ownloop-b193-r16.sh. No commits, no
  push. Heartbeats hb-r16-01..05 on file.
