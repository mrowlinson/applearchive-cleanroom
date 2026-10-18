# NOTE-scout-r32-regression: fresh r32 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r32/
  scratch (leg1/, leg2/, leg3/, leg-t2/,
  leg-t3/), TMPDIR r32/, oracle /usr/bin/aa.
  First-hand in r32, tip 142e8d4 (= r31
  baseline tip, no lane movement, worktree
  clean).
- T0-CONTAINER GREEN (x3 fresh-dir legs,
  rc=0 each).
- T1-CONTAINER GREEN (p0..p7, x3 fresh-dir
  legs, rc=0 each).
- T2-SEED7 GREEN (q0..q9 incl. q9 verify/fix,
  q7-seed).
- T3-SEED8 GREEN (same shape, disjoint seed).
- r31 lesson honored: one FRESH workdir per
  leg (t1-pinned.sh:130 mv reuse artifact
  avoided); no RED seen.
