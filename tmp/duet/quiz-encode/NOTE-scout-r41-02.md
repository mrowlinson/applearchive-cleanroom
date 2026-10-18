# NOTE-scout-r41-02: r41 CAP HANDOFF (no joint DONE, seat held, EXITING)

## r41 delivered (lanes/encode-container@142e8d4, clean, 0 commits)
1. Fresh r41 regression GREEN @142e8d4
   (NOTE-scout-r41-regression): T0 + T1 (x3
   fresh-dir legs, rc=0) + T2-SEED7 (88
   PASS) + T3-SEED8 (88 PASS), all GREEN
   banners first-hand on NVME r41/
   scratch. r7's landed tip re-verified; all 6
   per-codec rules + doc pin stay closed.
   r31 lesson honored (fresh workdir per leg);
   no RED seen.
2. Git identity r41 in TRUE worktree scope: `git
   config --worktree` for email (scout-r41@local)
   + user.name + commit.gpgsign false; verified
   WT resolves from config.worktree, common
   untouched. (--worktree used throughout per
   r20 lesson.)
3. CLAIM rolled r40 -> r41 at boot (filed
   immediately on start).
4. CMP donor re-checks (every round 1-30 +
   one deep all-file both-quiz grep): zero
   nonscout decmpfs/donor hits. PARKED.
   (Deep: enc 223 hits = scout's own notes
   only; dec donor = A-006 Oct-7 usage line,
   not a decmpfs donor.)
5. Polls 1-30 (sleep-30 each): Q frozen 364
   (newest Q-361 w2), A frozen 368 (newest A-367
   w2 geometry), decode 32Q/34A (newest Q-032/
   A-032), zero scout Qs (encode + decode
   quizzes), PARENT newest numbered 075
   (r12-exit, read r37-r40; binds this run via
   074 exit-at-cap: cap+handoff=EXIT; no 076+;
   REDIRECT-01 frontier-only read, viewer-seats
   scope, no scout action), DONE unchanged
   (w2s9 + writer1s3 enc; 7 decode DONEs).
   New traffic all other lanes' map work (cport
   r13 CAP 4/4 HANDOFF EXIT b227-b230 + 4
   merges GREEN, claim to r14; band229/band230
   + hb165/hb166; sweep2 r29 hb1/hb2 b224
   grinding GREEN + b226 pre-verified; sweep
   r16i hb2 b221 battery launched; viewer3 r14
   hb3 b220 CBAT+OWN green — all peeked,
   poll-clean for scout/kickoff/decmpfs, no
   scout relevance). All HITs: none (no
   self-HITs; own notes excluded from top-grep).
6. r40 predecessor line honored (HELD, 0 commits,
   regression GREEN, frozen inbox).

## Hygiene
- Nothing pushed; nothing committed (no changes
  needed); master HEAD 85abbbb (b209-b212 land;
  map-only anyway); no map-lane reads; TMPDIR on
  NVME (r41/); worktree clean @142e8d4.
  Heartbeats hb-r41-01..03 filed (seat-take +
  every ~8 rounds). Poll log: NVME encode-scout/
  r41/ poll.log (30 rounds).
- No /tmp use this round (no scratch slip).

## r42 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add
   per-chunk ZBM payload asserts to q8 lzbitmap cells
   (compare-only, hash-pin the dylib); if DENIED, mark
   DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with
   decode lane (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked;
   re-checked clean 30x + deep 1x in r41).
4. Solo-able: NONE queued — benefit matrix complete
   (6/6). r42 = regression upkeep + polls unless
   wall/kickoff/donor traffic lands. Candidate trivia
   if idle: single-chunk (stream<block) boundary-shape
   spot checks per codec. Reminder: fresh workdir
   per T0+T1 leg (t1-pinned.sh:130 mv artifact).
- CLOSED: v1/v2 selector (r5), lzfse 15/16 (r6),
  all-codec rules + census (r7).

## Refill requested
- Seat HELD, no joint DONE. Request r42 upkeep refill.
- EXITING per PARENT-074 (cap reached + handoff
  filed = EXIT; no hold-polling).
