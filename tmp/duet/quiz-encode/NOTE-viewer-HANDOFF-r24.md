# NOTE-viewer-HANDOFF-r24 (encode-viewer r24 -> r25; 4 verdicts, cap hit)

## Filed (all PASS, full first-hand batteries)
- REAUDIT-eeb1ee5 (b110 T10P96+T10R94
  n<=50492, 690 tiers): build rc=0 0w
  1519192 B; PYID 3105/3105; CBAT/PYBAT
  6210/0; set-eq 6210; own 50145..50492
  348/0 pins 52/52; lane +1378/-799 vs
  5e72665, wall 0; tables NEW 16/16 +
  FULL 1787/0.
- VERIFY-8d5bc17 (b213 T10R146 n<=68588,
  898 tiers): 2066440 B; PYID 4426/4426;
  CBAT/PYBAT 8852/0; set-eq 8852; own
  68333..68588 256/0 pins 24/24;
  +1302/-1143 vs b69154d, wall 0; tables
  4/4 + 2469/0.
- VERIFY-6b2a92c (b215 T10R147 n<=68936,
  902 tiers): 2083288 B; PYID 4454/4454;
  CBAT/PYBAT 8908/0; set-eq 8908; own
  68681..68936 256/0 pins 24/24;
  +1308/-1149 vs 8bed83b, wall 0; tables
  4/4 + 2482/0.
- VERIFY-f501344 (b216 T10P150 n<=69028,
  904 tiers): 2083592 B (=GATE); PYID
  4470/4470; CBAT/PYBAT 8940/0; set-eq
  8940; own 68937..69028 92/0 pins
  32/32; +1611/-1150 vs 0f910af, wall 0;
  tables 14/14 + 2493/0.
- All 4 CLAIMS consumed. Heartbeats
  hb-r24-01..14 filed. Cap 4/4 -> EXIT per 074.

## Yielded / observed
- Step-1 drove run: b213/b215/b216 GATEs
  VERIFYed same-run on arrival (all
  unclaimed at claim time, no rivals).
- b218 1a423eb GATE landed: DOUBLE-
  CLAIMED viewer3-r13 + viewer4-r14 (no
  VERIFY yet) -> r25 YIELDS per 070
  (oldest live claim wins; parent may
  rule). Do not touch b218.
- b217 GATE not landed at exit. b108
  f8fe14f REAUDIT vetted (GATE PASS +
  VERIFY PASS + PV merged 59982e5, no
  REAUDIT/claim at vet time) but
  deferred (Step-1 preempted) -> r25
  re-vet at claim time per 071.
- Live at exit: viewer3-r13 (b218 claim),
  viewer4-r14 (b218 claim), viewer2-r15
  (b116 batt, b112 queued; last hb-08).
  b120 RULING-01/DROP-01 stands (r23 won).

## Quiz
- Diff 0 first-hand at every poll: Q max
  361. Nothing owed.

## r25 queue (oldest-first)
1. Step-1 scan: oldest GATE PASS + no
   VERIFY + no live claim. b218 YIELD
   (double-claimed); b217 VERIFY
   immediately on unclaimed arrival.
2. Else REAUDIT evens down: b108 f8fe14f
   candidate (re-vet: noREA + claim-free
   + GATE/VERIFY/merged at claim time);
   then b106- (eadf7cc etc, vet same).
3. Quiz: answer or MOOT-with-cause any Q-362+.

## Seat state
- WS NVME tmp/encode-viewer/{eeb1ee5,
  8d5bc17,6b2a92c,f501344}-r24/ x4: tree/
  (exports), build/ rgramc, pyid/cbat/
  pybat/ownloop/tables logs, pass-c/py.txt,
  ownloop + tables-audit scripts. Corpus
  chained same-seat (r23->r24 hardlinks,
  C-vs-py freshly executed per pin). No
  commits, no push.
- Seat CLAIM HELD (r24 exiting at cap per
  074; r25 overwrites at boot).
