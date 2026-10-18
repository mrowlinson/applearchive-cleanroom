# NOTE-scout-r8-02: r8 REFILL HANDOFF (no joint DONE, seat held)

## r8 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r8 regression GREEN @142e8d4 (NOTE-r8-regression):
   T0 + T1 + T2-SEED7 + T3-SEED8, all rc=0 first-hand on
   NVME r8/ scratch. r7's landed tip re-verified; all 6
   per-codec rules + doc pin stay closed.
2. Git identity r8 in TRUE worktree scope (r8-01): caught +
   reverted a plain-`git-config` leak into common .git/config
   (would have hit main + all worktrees), then `git config
   --worktree`; verified WT resolves scout-r8@local from
   config.worktree, main back to global owner identity, no
   [user] in common config. LESSON for r9+: in a linked
   worktree ALWAYS use `git config --worktree`.
3. CMP donor re-check (round 7): no non-scout decmpfs/donor
   mentions in quiz. PARKED.
4. Polls 4-10 (sleep-60 each): inbox frozen (364 Q, newest
   Q-361 w2), zero scout Qs (encode + decode quizzes),
   PARENT newest 068 (viewer4, unrelated), DONE unchanged
   (w2s9 + writer1s3). Claim HELD for r9.

## Hygiene
- Nothing pushed; nothing committed (no changes needed);
  master untouched; no map-lane reads; TMPDIR on NVME (r8/);
  worktree clean @142e8d4. Heartbeats hb-r8-01..04 filed
  ~every 10 calls (this run: 3 notes + 4 heartbeats with
  this handoff).

## r9 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add per-chunk ZBM
   payload asserts to q8 lzbitmap cells (compare-only, hash-pin
   the dylib); if DENIED, mark DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with decode lane
   (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked; re-checked
   clean in r8 round 7).
4. Solo-able: NONE queued — benefit matrix complete (6/6).
   r9 = regression upkeep + polls unless wall/kickoff/donor
   traffic lands. Candidate trivia if idle: single-chunk
   (stream<block) boundary-shape spot checks per codec.
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6), all-codec
  rules + census (r7).
