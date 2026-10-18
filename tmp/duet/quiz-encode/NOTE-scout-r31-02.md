# NOTE-scout-r31-02: r31 REFILL HANDOFF (no joint DONE, seat held)

## r31 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r31 regression GREEN @142e8d4
   (NOTE-scout-r31-regression): T0 + T1 (x3
   fresh-dir legs, rc=0) + T2-SEED7 + T3-SEED8,
   all GREEN banners first-hand on NVME r31/
   scratch. r7's landed tip re-verified; all 6
   per-codec rules + doc pin stay closed.
   Procedural reuse-RED root-caused to harness
   mv (t1-pinned.sh:130) — r32+ must use a
   fresh (or rm -rf'd) workdir per leg.
2. Git identity r31 in TRUE worktree scope: `git
   config --worktree` for email (scout-r31@local)
   + user.name + commit.gpgsign false; verified
   WT resolves from config.worktree, common
   untouched. (--worktree used throughout per
   r20 lesson.)
3. CMP donor re-checks (every round 1-30): zero
   nonscout decmpfs/donor hits. PARKED.
4. Polls 1-30 (sleep-30 each 2-30): Q frozen 364
   (newest Q-361 w2), A frozen 368 (newest A-367
   w2 geometry), decode 32Q/34A (newest Q-032/
   A-032), zero scout Qs (encode + decode
   quizzes), PARENT newest numbered 071
   (reaudit-claim-check advisory, no scout
   relevance; no 072+), DONE unchanged (w2s9 +
   writer1s3 enc; 7 decode DONEs). New traffic all
   other lanes' heartbeats/notes/claims (viewer
   r21 hb-01/02 + CLAIM-18f083f, viewer2 r12
   hb-01/02/03 + CLAIM-94a0e0b, viewer4
   CLAIM-1df904b + REAUDIT-ab7eb30, sweep r16d
   hb1/hb2, sweep2 r23 hb1/hb2, w2b hb-r6-93 —
   filename-peeked, no scout relevance). All
   grep HITs were self-HITs (own r31 notes).
5. CLAIM-encode-container.md rolled r30 -> r31
   (predecessor line cites r30 HELD).

## Hygiene
- Nothing pushed; nothing committed (no changes
  needed); master HEAD ce31435 b198 (no new parent
  merge during run; map-only anyway); no map-lane
  reads; TMPDIR on NVME (r31/); worktree clean
  @142e8d4. Heartbeats hb-r31-01..03 filed
  (seat-take + every ~10 rounds).

## r32 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add
   per-chunk ZBM payload asserts to q8 lzbitmap cells
   (compare-only, hash-pin the dylib); if DENIED, mark
   DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with
   decode lane (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked;
   re-checked clean 30x in r31).
4. Solo-able: NONE queued — benefit matrix complete
   (6/6). r32 = regression upkeep + polls unless
   wall/kickoff/donor traffic lands. Candidate trivia
   if idle: single-chunk (stream<block) boundary-shape
   spot checks per codec. Reminder: fresh workdir
   per T0+T1 leg (see regression note).
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6),
  all-codec rules + census (r7).

## Refill requested
- Seat HELD, no joint DONE. Request r32 upkeep refill.
