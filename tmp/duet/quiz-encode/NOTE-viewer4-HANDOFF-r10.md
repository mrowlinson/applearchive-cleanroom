# NOTE-viewer4-HANDOFF-r10 (22 verdicts, exiting for refill)

## Filed (all PASS, full first-hand r10 batteries, all claims consumed)
- VERIFY-ff0c9c2 (b200): build
  2014632 B == GATE; PYID 4246/4246;
  CBAT/PYBAT 8492/0; set-eq; own
  66153..66244 92/0 p14 (=GATE 28/28
  x2); tables NEW 11/11 + FULL 2371;
  wall 0 vs 14531bb (+1556/-1095).
- VERIFY-7d6c9eb (b204): build
  2031832 B == GATE; PYID 4302/4302;
  8604/0; own 66849..66940 92/0 p16;
  tables 10/10 + 2398; wall 0 vs
  3b00b53 (+1557/-1109).
- VERIFY-ea56caf (b206): build
  2032232 B == GATE; PYID 4330/4330;
  8660/0; own 67197..67288 92/0 p16;
  tables 12/12 + 2413; wall 0 vs
  5be63bf (+1589/-1115).
- 19x REAUDIT odds b161..b125 (every
  odd band, all unsuffixed, zero
  races): 450255a/10c9f16/8ed30d1/
  c9dd7f8/c1cd305/885fc37/49f108c/
  fd438da/04cafeb/8af5995/d86b95a/
  c56c1e6/c91ee06/ab7eb30/1df904b/
  5db2d64/101d903/3621528/68d2eef.
  Each: build rc=0 0w; PYID full;
  CBAT/PYBAT full 0 FAIL; set-eq
  cmp-identical; own-loop 256/0;
  tables NEW+FULL 0-mismatch; wall 0.
  (Per-file legs in each REAUDIT.)

## Stood down (no duplicate batteries)
- b196/b198/b199/b201/b202/b203:
  all VERIFY-closed or live-claimed
  thru run (yielded correctly every
  time). b205 8b26a1f GATE-claimed
  (sweep) at exit. 13 ancient
  GATE-no-VERIFY excluded (owner call).

## Coordination
- Even/odd split with viewer r19/r20/
  r21 held all run (r19: b162..b152;
  r20: b150/b148; r21: b146/b144;
  r22 queued b142/b140) — zero
  collisions both directions, mutual
  handoff cites. PARENT-071 claim-
  check at every claim + pre-filing.

## Quiz
- Diff 0 entire run: newest Q-361 =
  A-361 paired (rechecked pre-filing
  x22). Nothing owed.

## r11 queue (oldest-first, CLAIM-first per PARENT-071)
1. Oldest GATE+no-VERIFY+no-live-claim
   (re-scan: b203/b205+ tip flow).
2. Else REAUDIT odds down: b123
   9e30e0b next, then b121 f7cf078
   (vet GATE+VERIFY+merged+claim-free
   at claim time; evens = viewer turf,
   expect r22 on b142/b140/b138...).
3. Quiz: answer or MOOT-with-cause any
   Q-362+.

## Seat state
- WS tmp/encode-viewer4/{reaudit,
  verify}-<hash>/ x22: tree/ (git
  archives), build/rgramc, work/
  (pyid/cbat/pybat/own/tables logs,
  c.names/p.names, tables-eq-r10.py,
  ownloop via shared ownloop.sh).
  Corpus 4101 .rav (r9 cache) retained
  for seeding. No commits, no push.
  Heartbeats hb-r10-01..24 filed.
