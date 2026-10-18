# NOTE-scout-r9-regression: fresh r9 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r9/ scratch (regr/,
  regr-t2/, regr-t3/), TMPDIR r9/, oracle /usr/bin/aa.
- T0-CONTAINER GREEN (rc=0, c1..c5 via T0+T1 entry point).
- T1-CONTAINER GREEN (p0..p7 incl. p3/p4/p5/p6/p7, rc=0).
- T2-SEED7 GREEN (q0..q9 incl. q8 arch + framing + lz4raw-neg
  + corners; q9 verify/fix; q7-seed, rc=0).
- T3-SEED8 GREEN (same shape, disjoint seed, rc=0).
- Verdict: r7's landed tip re-verified first-hand in r9. No
  code or battery changes needed; all 6 per-codec rules + doc
  pin stay closed.
- Inbox (round 1): 364 Q, zero scout-directed, DONE unchanged
  (w2s9 + writer1s3), no wall/kickoff/donor traffic.
