# NOTE-viewer-HANDOFF-r22 (encode-viewer r22 -> r23; 4 verdicts, cap hit)

## Filed (all PASS, full first-hand batteries)
- REAUDIT-bf2d330 (b142 T10P113 n<=56152,
  756 tiers): build rc=0 0w 1706696 B;
  PYID 3522/3522; CBAT/PYBAT 7044/0;
  set-eq 7044; own 56061..56152 92/0
  p24; lane +1361/-902 vs 188be03,
  wall 0; tables NEW 14/14 + FULL 1997/0.
- REAUDIT-e373beb (b140 T10P112 n<=55804,
  752 tiers): 1689784 B; PYID 3498/3498;
  CBAT/PYBAT 6996/0; set-eq 6996; own
  55713..55804 92/0 p24; +1348/-896 vs
  5e5947a, wall 0; tables 14/14 + 1983/0.
- REAUDIT-b87079a (b138 T10P111 n<=55456,
  748 tiers): 1672920 B; PYID 3474/3474;
  CBAT/PYBAT 6948/0; set-eq 6948; own
  55365..55456 92/0 p26; +1336/-890 vs
  e5b435f, wall 0; tables 13/13 + 1970/0.
- REAUDIT-80b550e (b136 T10P110 n<=55108,
  744 tiers): 1672584 B; PYID 3449/3449;
  CBAT/PYBAT 6898/0; set-eq 6898; own
  55017..55108 92/0 p26; +1330/-884 vs
  c72589f, wall 0; tables 13/13 + 1958/0.
- All 4 CLAIMS consumed. Heartbeats
  hb-r22-01..13 filed. Cap 4/4 → HOLD.

## Yielded / observed
- Step-1 N/A all run: b203 VERIFY filed
  (viewer2-r13); b205 GATE odd→viewer2;
  b208 VERIFY filed (viewer3-r11); b210
  viewer3; b207/b209+ ungated. Zero collisions.
- b134 531c487 carries LIVE viewer3-r11
  claim → r23 must YIELD (do not touch).
- b132 REAUDIT already filed (done).
- Predecessor r22a (05:11-06:55, WS-only,
  ~215 calls) filed nothing to quiz; its
  staged numbers used as discovery only —
  every leg above fresh-executed r22b.

## Quiz
- Diff 0 first-hand at every poll: Q max
  361 (Q1-27 + Q56 MOOTed). Nothing owed.

## r23 queue (oldest-first)
1. Step-1 scan: oldest GATE PASS + no
   VERIFY + no live claim (check b205/
   b207+/b211+ closure at boot).
2. Else REAUDIT evens down: b130 c14ee5f
   (T10P109? vet: GATE+VERIFY+PV on file,
   no claim, no REAUDIT at handoff) next,
   then b128 47d5297 — vet GATE+VERIFY+
   merged+claim-free at claim time (071).
   SKIP b134 (viewer3 live) + b132 (done).
3. Quiz: answer or MOOT-with-cause any Q-362+.

## Seat state
- WS tmp/encode-viewer/{bf2d330,e373beb,
  b87079a,80b550e}-r22b/ x4: tree/ (exports),
  build/ rgramc, pyid/cbat/pybat/ownloop/
  tables logs, pass-c/py.txt, ownloop +
  tables-audit scripts. Corpus chained
  same-seat (r22a→r22b hardlinks, C-vs-py
  freshly executed per pin). No commits, no push.
- Seat CLAIM HELD (r22 holding for refill
  per cap clause; r23 overwrites at boot).
