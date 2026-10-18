# NOTE-scout-r7-02: fresh r7 regression GREEN @7b3226e

- Gate: tests/test_container.sh on NVME r7/ scratch, oracle
  /usr/bin/aa macOS 27.0.1, adapter frame-archive path.
- T0-CONTAINER GREEN (rc=0).
- T1-CONTAINER GREEN (p0..p7 incl. p3/p4/p5/p6/p7, rc=0).
- T2-SEED7 GREEN 56/56 (q8 16 arch + framing + lz4raw-neg +
  2 corners; q9 8 cells; q7-seed), rc=0.
- T3-SEED8 GREEN 56/56 (same shape, disjoint seed), rc=0.
- Verdict: r6's landed tip re-verified first-hand in r7. No
  code or battery changes needed; v1/v2 + 15/16 pins stay closed.
- Inbox (round 3): 364 Q, zero scout-directed, DONE unchanged
  (w2s9 + writer1s3), no wall/kickoff/donor traffic.
