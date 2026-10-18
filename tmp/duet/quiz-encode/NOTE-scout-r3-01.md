# NOTE-scout-r3-01: seat open, r2 absorbed, T2 generator underway

- Seat: encode-container scout r3 (PARENT-067). Lane
  lanes/encode-container@4be6d90 clean; git identity worktree-local ok
  (inherited). TMPDIR .../encode-scout/r3 on NVME. Oracle:
  /usr/bin/aa macOS 27.0.1 (same build as L5/T1 pins).
- Quiz inbox checked: 364 Q-files, newest Q-361 w2 geometry — all
  map-turf, zero scout-directed. Q-23 grep hit is writer2 bitmap
  (map-turf, known since r2). DONE markers unchanged, no joint DONE.
- r2 absorbed: NOTE-r2-01..09 + hb-r2-01..08. Committed state
  verified: harness/container-adapter.sh (6 verbs), tests/container
  T0 5 cells + T1 27 cells, vectors/selfgen T1 pins (FIXTURES §8),
  pbz* derived spec + IDX-chain + HLC-close in notes.
- r3 plan (oldest-first per handoff): (1) T2 seeded-corpus
  generator (t2-gen.py) + runner (t2-seeded.sh) legs — sparse/
  clone/-b/-t/HLC/cpio-convert/omanifest-IDX cells per NOTE-04 §C
  + r2 NOTE-06..08 measurements; NVME-linked, quota-guarded,
  seed-parameterized so T3 = disjoint-seed rerun. (2) m/YAF hunt
  (check-and-fix on corrupted inputs?). (3) W/R/T+YAA1 acceptance
  (needs foreign bytes — probe solo, coordinate at kickoff).
  (4) lzbitmap chunk-oracle path (aa convert leg).
- Claim updated to r3. Heartbeat every ~10 calls. Stay-alive: 10
  rounds + sleep-60/poll; never exit pre-DONE.
