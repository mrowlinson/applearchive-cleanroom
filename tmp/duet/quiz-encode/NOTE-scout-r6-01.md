# NOTE-scout-r6-01: seat open, r5 absorbed, identity scope FIXED, queue polled

- Seat: encode-container scout r6 (PARENT-067). Lane
  lanes/encode-container@6be8a2b clean; TMPDIR .../encode-scout/r6
  on NVME. Oracle: /usr/bin/aa macOS 27.0.1.
- r5 absorbed: NOTE-r5-01..04,06 + hb-r5-01..06 + handoff r5-06.
  v1/v2 CLOSED (4095|4096), doc pin @6be8a2b, regression GREEN.
- IDENTITY FIX (r5's fix was wrong-scope): r5 set user.name/email
  in repo-level .git/config, so EVERY worktree without its own
  override inherited scout-r5 (verified: wt-encode-writer2b +
  all wt-pv-* resolved scout-r5@local). r6 moved it to TRUE
  worktree scope (`config --worktree` ->
  .git/worktrees/wt-encode-container/config.worktree,
  encode-container-scout/scout-r6@local) and UNSET the repo
  keys. Verified: container WT = r6 identity from config.worktree;
  main + writer2b + PV + cport WTs = global owner identity.
  Parent merges in main no longer author as scout.
- Quiz inbox checked: 364 Q-files, newest Q-361 w2 geometry —
  all map-turf, zero scout-directed (Q grep for scout: empty).
  DONE unchanged (w2s9 + writer1s3), no joint DONE. Decode-quiz
  grep for scout/kickoff/encode-container: empty.
- r6 queue poll (oldest-first): (1) wall ruling on r4-02
  libzbitmap COMPARE-ONLY: NO response filed (no PARENT/GRANT
  traffic, newest PARENT-068 is viewer4 redirect); (2) kickoff
  18-cell matrix: NO decode-lane traffic; (3) CMP donor: none
  appeared. All three externally gated — r6 runs fresh
  regression + solo-able raw-floor trivia + stay-alive polls.
- Claim updated to r6. Heartbeat every ~10 calls. Stay-alive:
  10 rounds + sleep-60/poll; never exit pre-DONE.
