# NOTE-scout-r5-02: fresh r5 regression GREEN @a13215e

- Gate: tests/test_container.sh on NVME r5/ scratch, oracle
  /usr/bin/aa macOS 27.0.1, adapter frame-archive path.
- T0-CONTAINER GREEN (c2/c3/c4/c5 PASS, rc=0).
- T1-CONTAINER GREEN (p5/p6/p7 PASS, rc=0).
- T2-SEED7 GREEN 56/56 (q8 16 arch + framing + lz4raw-neg +
  2 corners; q9 8 cells; q7-seed), rc=0.
- T3-SEED8 GREEN 56/56 (same shape, disjoint seed), rc=0.
- Verdict: r4's landed tip re-verified first-hand in r5. No
  code or battery changes needed; G4 stays closed.
- Inbox (round 3): 364 Q, zero scout-directed, DONE unchanged
  (w2s9 + writer1s3), no wall/kickoff/donor traffic.
