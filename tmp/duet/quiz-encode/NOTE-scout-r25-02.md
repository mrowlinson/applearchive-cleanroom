# NOTE-scout-r25-02: r25 REFILL HANDOFF (no joint DONE, seat held)

## r25 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r25 regression GREEN @142e8d4
   (NOTE-scout-r25-regression): T0 + T1 (x3 legs) +
   T2-SEED7 + T3-SEED8, all GREEN banners
   first-hand on NVME r25/ scratch. r7's landed
   tip re-verified; all 6 per-codec rules + doc
   pin stay closed.
2. Git identity r25 in TRUE worktree scope: `git
   config --worktree` for email (scout-r25@local)
   + user.name + commit.gpgsign false; verified WT
   resolves from config.worktree, common untouched.
   (No mis-scope this run: --worktree used
   throughout per r20 lesson.)
3. CMP donor re-checks (every round 1-30): zero
   nonscout decmpfs/donor hits. PARKED.
4. Polls 1-30 (sleep-30 each 2-30): Q frozen 364
   (newest Q-361 w2), A frozen 368 (newest A-367
   w2 geometry), decode 32Q/34A (newest Q-032/
   A-032), zero scout Qs (encode + decode
   quizzes), PARENT newest 071 (reaudit-claim-check
   advisory, no scout relevance; no 072+), DONE
   unchanged (w2s9 + writer1s3). New traffic all
   other lanes' heartbeats/claims (viewer ef0144b-r16
   claim + hb-r16-01/02 + r15 HANDOFF, viewer2 r10
   hb-05, viewer3 r9 hb-01..03, viewer4 r8 hb-04 +
   HANDOFF + REAUDIT-fac36c9, sweep r14 hb3..hb5 +
   ef0144b claim, sweep2 r19 hb3 + 676626e claim,
   w2 r13 hb-17/18, w2b r6 hb-51/52, GATE-bd1ca6d +
   GATE-94a0e0b — all filename-peeked, no scout
   relevance). All grep HITs were self-HITs (own
   r25 notes).
5. CLAIM-encode-container.md rolled r24 -> r25
   (predecessor line cites r24 HELD).

## Hygiene
- Nothing pushed; nothing committed (no changes
  needed); master untouched (HEAD 9633edf b190,
  same as r24 baseline — zero new parent merges
  during run, map-only anyway); no map-lane reads;
  TMPDIR on NVME (r25/); worktree clean @142e8d4.
  Heartbeats hb-r25-01..03 filed (seat-take +
  every ~10 rounds).

## r26 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add
   per-chunk ZBM payload asserts to q8 lzbitmap cells
   (compare-only, hash-pin the dylib); if DENIED, mark
   DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with
   decode lane (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked;
   re-checked clean 30x in r25).
4. Solo-able: NONE queued — benefit matrix complete
   (6/6). r26 = regression upkeep + polls unless
   wall/kickoff/donor traffic lands. Candidate trivia
   if idle: single-chunk (stream<block) boundary-shape
   spot checks per codec.
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6),
  all-codec rules + census (r7).

## Refill request
- Seat HELD, no joint DONE: request r26 scout refill
  (same brief shape, claim roll r25->r26, fresh
  regression on r26/ scratch first).
