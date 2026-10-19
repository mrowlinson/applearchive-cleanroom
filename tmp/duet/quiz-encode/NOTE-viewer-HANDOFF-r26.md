# NOTE-viewer-HANDOFF-r26 (encode-viewer r26 -> r27; 2 verdicts + 8 quiz, EXIT, cap open)

## Filed (all PASS, full first-hand batteries)
- VERIFY-8289f49 (b228 T10P156
  n<=71116, 928 tiers): build rc=0 0w
  2151928 B == GATE; PYID 4638/4638;
  CBAT/PYBAT 9276/0; set-eq 9276; own
  71025..71116 92/0 pins 32/32;
  lane +1663/-1190 vs f9ad84f, wall 0;
  tables NEW 15/15 + FULL 2577/0.
- VERIFY-854478f (b230 T10P157
  n<=71464, 932 tiers): 2168792 B ==
  GATE; PYID 4666/4666; CBAT/PYBAT
  9332/0; set-eq 9332; own 71373..71464
  92/0 pins 32/32; +1658/-1198 vs
  6ca2150, wall 0; tables 14/14 + 2591/0.
- Both CLAIMS consumed. Heartbeats
  hb-r26-01..16 filed. EXIT at 2/4:
  no eligible work (see below), holding
  would starve rotation per 074 spirit.

## Quiz (8 CONFIRM, all first-hand)
- A-368..375 answer Q-362..369 (w2d-r1
  T10P501..P508): CONFIRM all (36+35+
  25+28+26+25+28+27 checks) from own
  2786-cell oracle bed 191085..193522.
  Bed+scripts NVME encode-viewer/
  q362-r26/ (census*.sh, analyze*.py).
- Findings: ring m-index = o%16;
  consts base 86 excl b4/b5 (fits all
  20 blocks); P508 head bodies fill
  writer TBD (32/84 + 55/84).
- Q max 369, A max 375, diff 0 at exit.
  w2d-r1 Q-phase done (8/8), now
  RECORD/splice/commit.

## Yielded / observed
- b218 1a423eb: NEVER-TOUCHED per
  brief. NOTE: viewer4-r14 DROPPED per
  DROP-02 (claim VACATED); successor
  r15 NOT filed at exit -> b218 has NO
  live claim. r27: do NOT auto-claim;
  never-touch order + r15 assignment
  stand until parent clarifies. Re-vet.
- b225 99edcde STILL UNGATED at exit
  (sweep r16j dark 7.5h since hb2
  00:32, battery running-or-dead).
  b228/b230 VERIFYed ahead of it
  (self-contained, b219-precedent).
- REDIRECT-01 frontier-only honored all
  run: zero REAUDIT claims.
- Live at exit: viewer3-r16 (yields
  b228/b230 to my older claims per
  070, polling b225); sweep r16j
  (dark); sweep2-r30 EXITed (r31/b232
  efc0366 not booted); w2d-r1 splicing.

## r27 queue (oldest-first)
1. Step-1 scan: oldest GATE PASS + no
   VERIFY + no live claim. b225
   99edcde VERIFY on unclaimed arrival
   (watch viewer3-r16: oldest claim
   wins per 070); then newest GATEs
   (b232+ as landed). b218: see above.
2. REAUDIT: BANNED per REDIRECT-01 until
   parent lifts.
3. Quiz: answer or MOOT-with-cause any
   Q-370+ (w2d-r1 RECORD phase may ask
   splice Qs; bed extendable to 193870+).

## Seat state
- WS NVME tmp/encode-viewer/{8289f49,
  854478f}-r26/ x2: tree/ (exports),
  build/ rgramc, pyid/cbat/pybat/
  ownloop/tables logs, pass-c/py.txt,
  ownloop + tables-audit scripts. Corpus
  chained r25->r26 hardlinks, C-vs-py
  freshly executed per pin. q362-r26/
  quiz bed (2786 cells) reusable.
- Seat CLAIM HELD (r26 exiting per 074
  spirit at 2/4; r27 overwrites at boot).
- No commits, no push.
