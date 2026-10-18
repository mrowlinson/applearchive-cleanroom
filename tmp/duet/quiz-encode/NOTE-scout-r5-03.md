# NOTE-scout-r5-03: lzfse v1/v2 selector CLOSED — exact threshold 4096

## Rule (measured, oracle /usr/bin/aa macOS 27.0.1, own bytes)
Per-chunk payload version keys EXACTLY on uncompressed length u:
u <= 4095 -> v1 (bvxn), u >= 4096 -> v2 (bvx2). Position-independent
(single/tail/full all agree). Closes r2-06's open interval
(2445,4096] to the exact step 4095|4096.

## Evidence (NVME r5/v12/, -a lzfse -t 1, pattern files, end==size all)
- Coarse: 34 single-chunk archives u=2444..4094 step 50 -> ALL v1.
- Bisect: u=4094 v1 (single N=3850 + tail N=7946); u=4095 v1
  (single N=3851 + tail N=7947); u=4096 v2 (single N=3852 +
  last-full N=7948 + non-last-full chunk0s). Clean step, no fuzz.
- Anchors: -b 1k full-1024 chunks v1 (reconfirms r2-06); -b 64k
  full-65536 v2 + tail-4710 v2 (tails CAN be v2 when >= 4096).
- Framing: stream = N + 244 exactly across the sweep (one 246
  sighting at N=70000 — overhead grows with magnitude width,
  linearity holds within a sweep).

## Incidental (not pursued)
- 1-byte tail (N=3853, u=1 c=1) stored RAW (payload = raw byte).
  Raw-store rule already generalized (r4-04); the raw-vs-coded
  floor is a separate trivia, untouched.
- Decoder rule unchanged and firm: accept both magics per chunk.

## Container-lane consequence
- Encoder-side: chunks with u >= 4096 MUST be written v2,
  u <= 4095 MUST be v1 for oracle-identical bytes. Filed as
  trivia; FIXTURES threshold note update queued as a doc commit
  if r5 lands anything else (no code impact — battery has no
  v1/v2 assert cells, and none are needed: framing/census cover it).
- Inbox (round 6): 364 Q, zero scout-directed, DONE unchanged,
  no wall/kickoff/donor traffic.
