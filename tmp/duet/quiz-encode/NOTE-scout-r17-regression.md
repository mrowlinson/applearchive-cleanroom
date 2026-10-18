# NOTE-scout-r17-regression: fresh r17 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r17/
  scratch (regr/, regr-t2/, regr-t3/),
  TMPDIR r17/, oracle /usr/bin/aa. First-hand
  in r17, tip 142e8d4.
- T0-CONTAINER GREEN (t0-smoke rc=0 x3: base +
  T2 + T3 legs).
- T1-CONTAINER GREEN (p0..p7 incl. p3/p4/p5/p6/
  p7, x3 legs).
- T2-SEED7 GREEN (q0..q9 incl. q8 arch + framing
  + lz4raw-neg + corners; q9 verify/fix; q7-seed).
- T3-SEED8 GREEN (same shape, disjoint seed).
- Verdict: r7's landed tip re-verified first-hand
  in r17. No code or battery changes needed; all
  6 per-codec rules + doc pin stay closed.
- Inbox (round 1): 364Q/368A frozen, zero scout-
  directed, PARENT newest 069 (b180-verify ruling,
  no scout relevance), DONE unchanged (w2s9 +
  writer1s3), no wall/kickoff/donor traffic (CMP
  PARKED).
