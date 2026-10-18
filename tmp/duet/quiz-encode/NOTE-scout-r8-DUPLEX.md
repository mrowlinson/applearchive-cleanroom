# NOTE-scout-r8-DUPLEX: duplicate r8 launch yields to live seat holder

- This invocation (2nd r8 launch) found the seat OCCUPIED: live r8
  agent filed NOTE-scout-r8-01 (22:31), NOTE-scout-r8-regression +
  hb-r8-01 (22:32), CLAIM-encode-container.md fresh, regression
  outputs actively landing in .../encode-scout/r8/.
- Per claim protocol (yield to fresh/live claim): this duplicate
  exits COVERED without touching TMPDIR r8/, lane, or NOTE
  numbering. No work lost — live agent is executing the brief.
- Parent: refill this worker elsewhere; do NOT relaunch scout r8.
