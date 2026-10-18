# NOTE-scout-r37-regression: fresh r37 regression GREEN @142e8d4

- Gate: tests/test_container.sh on NVME r37/
  scratch (leg1/, leg2/, leg3/, leg-t2/,
  leg-t3/), TMPDIR r37/, oracle /usr/bin/aa.
  First-hand in r37, tip 142e8d4 (= r36
  baseline tip, no lane movement, worktree
  clean).
- T0-CONTAINER GREEN (x3 fresh-dir legs,
  rc=0 each).
- T1-CONTAINER GREEN (p0..p7, x3 fresh-dir
  legs, rc=0 each).
- T2-SEED7 GREEN (88 PASS, rc=0).
- T3-SEED8 GREEN (88 PASS, rc=0).
- r31 lesson honored: one FRESH workdir per
  leg (t1-pinned.sh:130 mv reuse artifact
  avoided); no RED seen.
