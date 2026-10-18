# NOTE-scout-r6-02: fresh r6 regression GREEN @6be8a2b

- Gate: tests/test_container.sh on NVME r6/ scratch, oracle
  /usr/bin/aa macOS 27.0.1, adapter frame-archive path.
- T0-CONTAINER GREEN (gate reached T1, rc=0).
- T1-CONTAINER GREEN (p3/p4/p5/p6/p7 PASS, rc=0).
- T2-SEED7 GREEN 56/56 (q8 16 arch + framing + lz4raw-neg +
  2 corners; q9 8 cells; q7-seed), rc=0.
- T3-SEED8 GREEN 56/56 (same shape, disjoint seed), rc=0.
- Verdict: r5's landed tip re-verified first-hand in r6. No
  code or battery changes needed; v1/v2 pin + G4 stay closed.
- Inbox (round 3): 364 Q, zero scout-directed, DONE unchanged
  (w2s9 + writer1s3), no wall/kickoff/donor traffic.
