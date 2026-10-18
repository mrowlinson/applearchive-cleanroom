# NOTE-scout-r37-02: r37 CAP HANDOFF (no joint DONE, seat held, EXITING)

## r37 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r37 regression GREEN @142e8d4
   (NOTE-scout-r37-regression): T0 + T1 (x3
   fresh-dir legs, rc=0) + T2-SEED7 (88
   PASS) + T3-SEED8 (88 PASS), all GREEN
   banners first-hand on NVME r37/
   scratch. r7's landed tip re-verified; all 6
   per-codec rules + doc pin stay closed.
   r31 lesson honored (fresh workdir per leg);
   no RED seen.
2. Git identity r37 in TRUE worktree scope: `git
   config --worktree` for email (scout-r37@local)
   + user.name + commit.gpgsign false; verified
   WT resolves from config.worktree, common
   untouched. (--worktree used throughout per
   r20 lesson.)
3. CLAIM rolled r36 -> r37 at boot (filed
   immediately on start).
4. CMP donor re-checks (every round 1-30): zero
   nonscout decmpfs/donor hits. PARKED.
5. Polls 1-30 (sleep-30 each 2-30): Q frozen 364
   (newest Q-361 w2), A frozen 368 (newest A-367
   w2 geometry), decode 32Q/34A (newest Q-032/
   A-032), zero scout Qs (encode + decode
   quizzes), PARENT newest numbered 075
   (r12-exit, viewer4-only, read; binds this
   run via 074 exit-at-cap: cap+handoff=EXIT;
   no 076+), DONE unchanged (w2s9 +
   writer1s3 enc; 7 decode DONEs). New traffic all
   other lanes' map work (viewer3 hb-r12-12 b212
   PYID running; sweep2 hb-r26-7 b214 gate-tip
   RGRAM 6560/8884 0 FAIL; sweep hb-r16f-11 b211
   RGRAM 50% 0 FAIL; viewer4 hb-r13-02 b115 batt
   1/4 legs running — all peeked, grep-clean for
   scout/container/kickoff/decmpfs, no
   scout relevance). Rounds 11-30 fully static.
   Q-23 grep HIT = ancient map prose (ZBM vs
   container), not scout traffic. All other HITs
   were self-HITs (own r37 notes).
6. r36 predecessor line honored (HELD, 0 commits,
   regression GREEN, frozen inbox).

## Hygiene
- Nothing pushed; nothing committed (no changes
  needed); master HEAD edf09a9 (b207+b208 land;
  map-only anyway); no map-lane reads; TMPDIR on
  NVME (r37/); worktree clean
  @142e8d4. Heartbeats hb-r37-01..03 filed
  (seat-take + every ~10 rounds). Poll log:
  NVME encode-scout/r37/ poll.log (30 rounds).
- Scratch slip: leg1-3 logs first wrote /tmp
  (FORBIDDEN local temp); moved to NVME r37/
  same turn, /tmp verified clean after. No
  recurrence (T2/T3 direct to NVME).

## r38 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add
   per-chunk ZBM payload asserts to q8 lzbitmap cells
   (compare-only, hash-pin the dylib); if DENIED, mark
   DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with
   decode lane (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked;
   re-checked clean 30x in r37).
4. Solo-able: NONE queued — benefit matrix complete
   (6/6). r38 = regression upkeep + polls unless
   wall/kickoff/donor traffic lands. Candidate trivia
   if idle: single-chunk (stream<block) boundary-shape
   spot checks per codec. Reminder: fresh workdir
   per T0+T1 leg (t1-pinned.sh:130 mv artifact).
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6),
  all-codec rules + census (r7).

## Refill requested
- Seat HELD, no joint DONE. Request r38 upkeep refill.
- EXITING per PARENT-074 (cap reached + handoff
  filed = EXIT; no hold-polling).
