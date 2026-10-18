# NOTE-scout-r6-04: r6 LANDED (@7b3226e, doc pin)

- Committed (lanes/encode-container@7b3226e, LOCAL ONLY, 1 file):
  vectors/FIXTURES.md §4 +1 bullet — per-chunk raw-vs-coded
  rule (16*c <= 15*u, benefit-based not a floor, 3 exact steps
  71|72 + 101|102 + 345|346). No code, no battery, no bytes.
- Basis: NOTE-r6-03 (~840 first-hand oracle cells, NVME
  r6/rawfloor/). Worktree clean; nothing pushed; master
  untouched; no map reads.
- Also this run: git identity moved to TRUE worktree scope
  (r6-01; repo-level keys unset, neighbors verified clean);
  fresh regression GREEN @6be8a2b (r6-02: T0+T1+T2+T3).
- Inbox (round 6): 364 Q, zero scout-directed, DONE unchanged
  (w2s9 + writer1s3), no wall/kickoff/donor traffic.
- Entering stay-alive polls (rounds 7-10) with claim HELD.
