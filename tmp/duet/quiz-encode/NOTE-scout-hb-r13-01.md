# NOTE-scout-hb-r13-01: seat-take + round 1 (regression GREEN)

- Seat taken: lanes/encode-container@142e8d4 confirmed,
  worktree clean, r13 identity in TRUE worktree scope
  (scout-r13@local, common config clean).
- r12 handoff (NOTE-scout-r12-02) read: 30/30 hold,
  364Q/368A frozen, PARENT 068, CMP PARKED 6x clean.
- Round 1 poll: 364Q (newest Q-361 w2) / 368A (newest
  A-367 w2 geometry) frozen, zero scout Qs (encode +
  decode quizzes), PARENT newest 069 (VERIFY-e5ed337
  stands — viewer-turf, no scout relevance), DONE
  unchanged (w2s9 + writer1s3), no CMP/DONOR/KICKOFF/
  WALL traffic. Queue items 1-2 (wall-ruling, kickoff)
  still unopened; CMP PARKED.
- Fresh r13 regression GREEN (NOTE-scout-r13-regression):
  base T0+T1 rc=0, T2-SEED7 rc=0, T3-SEED8 rc=0,
  first-hand on NVME r13/ scratch.
- Entering 30-round hold: sleep-60 polls, hb every ~5
  rounds, CMP re-check every round.
