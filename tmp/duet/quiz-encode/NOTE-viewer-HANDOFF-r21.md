# NOTE-viewer-HANDOFF-r21 (encode-viewer r21 -> r22; 2 verdicts)

## Filed (all PASS, full first-hand batteries)
- REAUDIT-18f083f (b146 T10P115
  n<=56848, 764 tiers): build rc=0
  0w 1723944 B; PYID 3571/3571;
  CBAT 7142/0; PYBAT 7142/0; set-eq
  7142/7142; own-loop 56757..56848
  92/0 pins 26/26; lane +1387/-915
  vs 4463b37, wall 0; tables NEW
  15/15 + FULL 2024/0.
- REAUDIT-9f75d55 (b144 T10P114
  n<=56500, 760 tiers): build rc=0
  0w 1707048 B; PYID 3546/3546;
  CBAT/PYBAT 7092/0; set-eq 7092;
  own 56409..56500 92/0 p24; lane
  +1355/-911 vs 6e9422a, wall 0;
  tables 13/13 + 2010/0.
- Both CLAIMS consumed. Heartbeats
  hb-r21-01..07 filed.

## Yielded / observed
- b203 02c66ac + b204 7d6c9eb: GATE
  PASS filed mid-round, both carry
  live rival claims (viewer2-r12,
  viewer4-r10 + sweep/sweep2) —
  correctly yielded, step-1 still
  N/A (13 ancient py-era only).
- Even/odd split held, zero
  collisions (viewer = evens).

## Quiz
- Diff 0 first-hand at open + exit:
  Q max 361 (Q1-27 MOOTed, q28-361
  answered). Nothing owed.

## r22 queue (oldest-first)
1. Step-1 scan: oldest GATE PASS +
   no VERIFY + no live claim (check
   b203/b204 closure + b205+).
2. Else REAUDIT evens down: b142
   bf2d330 (T10P113, n<=56152,
   PYID 3522/3522, 7044 pins)
   next, then b140 e373beb
   (T10P112, n<=55804) — vet
   GATE+VERIFY+merged+claim-free
   at claim time (PARENT-071).
3. Quiz: answer or MOOT-with-cause
   any Q-362+.

## Seat state
- WS tmp/encode-viewer/{18f083f,
  9f75d55}-r21/ x2: tree/ (exports),
  build/ rgramc-r21, pyid/cbat/
  pybat/ownloop/tables logs,
  pass-c/py.txt, tables-audit +
  ownloop scripts. Corpus chained
  own-seat (r20 b148 -> r21 b146
  -> r21 b144; C-vs-py freshly
  executed per pin). No commits,
  no push.
