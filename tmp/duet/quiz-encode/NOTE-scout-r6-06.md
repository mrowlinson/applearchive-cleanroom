# NOTE-scout-r6-06: r6 REFILL HANDOFF (no joint DONE, seat held)

## r6 delivered (lanes/encode-container@7b3226e, LOCAL ONLY, 1 commit)
1. Raw-vs-coded chunk rule CLOSED (r6-03): code iff 16*c <= 15*u
   (saves >= 1/16), else RAW. Benefit-based, NOT a size floor:
   steps at 71|72 (zeros, c=67), 101|102 (phrase, c=95),
   345|346 (cycle256, c=324) — 3/3 exactly on the 15/16 line,
   ~840 first-hand oracle cells, zero anomalies. Every chunk,
   -b 1k + 4k agree. Alternatives excluded (floor, pure
   benefit, margin, 7/8, 31/32).
2. Doc pin landed (7b3226e, FIXTURES.md §4 +1 bullet). No code,
   battery, or bytes touched.
3. Fresh r6 regression GREEN @6be8a2b (r6-02): T0 + T1 +
   T2-SEED7 56/56 + T3-SEED8 56/56, all rc=0 first-hand.
4. Git identity moved to TRUE worktree scope (r6-01): r5's fix
   sat in repo-level .git/config and leaked scout-r5 into
   writer2b + all PV worktrees + parent merges. Now in
   config.worktree (scout-r6@local), repo keys unset, neighbors
   verified back on global identity.
5. CMP donor re-check (round 9): no donor traffic either quiz
   (`cmp` hits = byte-compare command), xattr spot re-check
   clean. Item stays PARKED.
6. Polls 7-10 (sleep-60 each): inbox frozen, zero scout Qs
   (encode + decode quizzes), DONE unchanged (w2s9 +
   writer1s3). Claim HELD for r7.

## Hygiene
- Nothing pushed; master untouched; no map-lane reads; TMPDIR on
  NVME (r6/); worktree clean @7b3226e. Heartbeats hb-r6-01..07
  filed ~every 10 calls (this run: 5 notes + 7 heartbeats with
  this handoff).

## r7 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add per-chunk ZBM
   payload asserts to q8 lzbitmap cells (compare-only, hash-pin
   the dylib); if DENIED, mark DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with decode lane
   (their craft harness); file verdicts.
3. CMP re-test if a decmpfs donor appears (parked, NOTE-r3-07;
   re-checked clean in r6 round 9).
4. Optional solo-able: other codecs' raw-vs-coded benefit lines
   (r6-03 follow-up: per-codec chunk-magic census first, then
   same sweep shape with codec= flag).
- v1/v2 selector: CLOSED (r5). Raw-vs-coded (lzfse): CLOSED (r6).
