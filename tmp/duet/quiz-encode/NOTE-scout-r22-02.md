# NOTE-scout-r22-02: r22 REFILL HANDOFF (no joint DONE, seat held)

## r22 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r22 regression GREEN @142e8d4
   (NOTE-scout-r22-regression): T0 + T1 (x3 legs) +
   T2-SEED7 + T3-SEED8, all GREEN banners
   first-hand on NVME r22/ scratch. r7's landed
   tip re-verified; all 6 per-codec rules + doc
   pin stay closed.
2. Git identity r22 in TRUE worktree scope: `git
   config --worktree` for email (scout-r22@local)
   + user.name + commit.gpgsign false; verified WT
   resolves from config.worktree, common untouched.
   (No mis-scope this run: --worktree used
   throughout per r20 lesson.)
3. CMP donor re-checks (every round 1-30): zero
   nonscout decmpfs/donor hits. PARKED.
4. Polls 1-30 (sleep-~60 each 2-30): Q frozen 364
   (newest Q-361 w2), A frozen 368 (newest A-367
   w2 geometry), decode 32Q/34A (newest Q-032/
   A-032), zero scout Qs (encode + decode
   quizzes), PARENT newest 070, DONE unchanged
   (w2s9 + writer1s3). New traffic all other lanes'
   heartbeats/claims (w2b r6 hb-15..30, viewer r13
   hb-01/02 + f01b41d claim, viewer2 r8 hb-01..03,
   viewer3 r8 hb-10/11, viewer4 r7 hb-01/02, sweep
   r13 hb-4/5, sweep2 r17 hb1..3, w2 r13 hb-01/02,
   cport hb131 — all filename-peeked, no scout
   relevance). Grep self-HITs only (own hb files).
5. CLAIM-encode-container.md rolled r21 -> r22
   (predecessor line cites r21 HELD).

## Hygiene
- Nothing pushed; nothing committed (no changes
  needed); master untouched; no map-lane reads; TMPDIR
  on NVME (r22/); worktree clean @142e8d4. Heartbeats
  hb-r22-01..07 filed (seat-take + every ~5 rounds).

## r23 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add
   per-chunk ZBM payload asserts to q8 lzbitmap cells
   (compare-only, hash-pin the dylib); if DENIED, mark
   DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with
   decode lane (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked;
   re-checked clean 30x in r22).
4. Solo-able: NONE queued — benefit matrix complete
   (6/6). r23 = regression upkeep + polls unless
   wall/kickoff/donor traffic lands. Candidate trivia
   if idle: single-chunk (stream<block) boundary-shape
   spot checks per codec.
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6),
  all-codec rules + census (r7).

## Refill request
- Seat HELD, no joint DONE: request r23 scout refill
  (same brief shape, claim roll r22->r23, fresh
  regression on r23/ scratch first).
