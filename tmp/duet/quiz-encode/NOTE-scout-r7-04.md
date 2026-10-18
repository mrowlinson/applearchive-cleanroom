# NOTE-scout-r7-04: r7 LANDED (@142e8d4, doc pin)

- Committed (lanes/encode-container@142e8d4, LOCAL ONLY, 1 file):
  vectors/FIXTURES.md §4 +1 bullet + 1 pointer edit — per-codec
  raw-vs-coded rules (shared 15/16 comparator; lzma/lzraven/zlib
  exact steps; lz4 per-u-c note; lzbitmap u>=145 floor + benefit
  half; payload magics incl. NEW bv41). No code, no battery, no
  bytes. Author scout-r7@local, worktree scope verified.
- Basis: NOTE-r7-03 (~480 first-hand oracle cells, NVME
  r7/census/ + r7/benefit/). Worktree clean; nothing pushed;
  master untouched; no map reads.
- Also this run: fresh regression GREEN @7b3226e (r7-02:
  T0+T1+T2+T3); seat open + queue poll (r7-01).
- Entering stay-alive polls (rounds 7-10) with claim HELD.
