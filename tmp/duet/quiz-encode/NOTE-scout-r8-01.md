# NOTE-scout-r8-01: seat open, r7 absorbed, queue polled, identity r8

- Seat: encode-container scout r8 (PARENT-067). Lane
  lanes/encode-container@142e8d4 clean; TMPDIR .../encode-scout/r8
  on NVME. Oracle: /usr/bin/aa macOS 27.0.1.
- r7 absorbed: NOTE-r7-01..05 + hb-r7-01..05. Per-codec
  raw-vs-coded CLOSED (all 6), doc pin @142e8d4, regression
  GREEN, identity TRUE worktree scope.
- IDENTITY: plain `git config` in a linked worktree writes the
  COMMON .git/config (leaked scout-r8 to main) — caught and
  reverted; then `git config --worktree user.email
  scout-r8@local`. Verified: WT resolves name+email from
  config.worktree; main resolves global owner identity; no
  [user] in common config. Neighbors untouched.
- Quiz inbox checked: 364 Q-files, newest Q-361 w2 geometry —
  all map-turf, zero scout-directed (Q grep for scout: empty).
  DONE unchanged (w2s9 + writer1s3), no joint DONE. Decode-quiz
  (newest Q-032 Oct 8) grep for scout/kickoff/encode-container:
  empty.
- r8 queue poll (oldest-first): (1) wall ruling on r4-02
  libzbitmap COMPARE-ONLY: NO response filed (newest PARENT-068
  is viewer4 order, unrelated); (2) kickoff 18-cell matrix: NO
  decode-lane traffic; (3) CMP donor: re-check scheduled
  mid-run per r6/r7 pattern. All three externally gated —
  r8 = fresh regression @142e8d4 + polls unless
  wall/kickoff/donor traffic lands. Solo queue: NONE (6/6
  benefit rules closed in r7).
- Claim updated to r8. Heartbeat every ~10 calls. Stay-alive:
  10 rounds + sleep-60/poll; never exit pre-DONE.
